from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext

from gevent import Greenlet
from redis import Redis


def chat(request):
    """Render the chat page."""
    return render_to_response('chatapp1/chat.html', {}, RequestContext(request))


def socketio(request):
    """The socket.io view."""
    io = request.environ['socketio']
    redis_sub = redis_client().pubsub()
    user = username(request.user)

    # Subscribe to incoming pubsub messages from redis.
    def subscriber(io):
        redis_sub.subscribe(room_channel())
        redis_client().publish(room_channel(), user + ' connected.')
        while io.connected():
            for message in redis_sub.listen():
                if message['type'] == 'message':
                    io.send(message['data'])
    greenlet = Greenlet.spawn(subscriber, io)

    # Listen to incoming messages from client.
    while io.connected():
        message = io.recv()
        if message:
            redis_client().publish(room_channel(), user + ': ' + message[0])

    # Disconnected. Publish disconnect message and kill subscriber greenlet.
    redis_client().publish(room_channel(), user + ' disconnected')
    greenlet.throw(Greenlet.GreenletExit)

    return HttpResponse()


def redis_client():
    """Get a redis client."""
    return Redis(settings.REDIS_HOST, settings.REDIS_PORT, settings.REDIS_DB,
                 socket_timeout=0.5)


def username(user):
    if user.is_authenticated():
        return user.username
    else:
        return 'guest-{n}'.format(n=redis_client().incr('chat:anonid'))


def room_channel(name='default'):
    """Get redis pubsub channel key for given chat room."""
    return 'chat:rooms:{n}'.format(n=name)
