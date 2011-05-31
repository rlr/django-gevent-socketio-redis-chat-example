from django.conf import settings
from django.core.handlers.wsgi import WSGIHandler
from django.core.cache import cache
from django.core.management.base import BaseCommand, CommandError

from gevent import monkey
from socketio import SocketIOServer

class Command(BaseCommand):
    args = '<port_number>'
    help = 'Start the chat server. Takes an optional arg (port #).'

    def handle(self, *args, **options):
        """Run gevent socketio server."""
        try:
            port = int(args[0])
        except:
            port = 8000

        # Make blocking calls in socket lib non-blocking:
        monkey.patch_all()

        # Start up gevent-socketio stuff
        application = WSGIHandler()
        print 'Listening on http://127.0.0.1:%s and on port 843 (flash policy server)' % port
        SocketIOServer(('', port), application, resource='socket.io').serve_forever()
