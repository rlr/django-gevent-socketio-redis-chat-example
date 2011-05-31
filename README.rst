=========================================
django-gevent-socketio-redis-chat-example
=========================================

This is an example of using django and gevent-socketio to build a chat
application using redis as the backend.

------------
Installation
------------

Note: you probably want to create and activate a virtualenv before
running installing the requirements below. I use and like virtualenvwrapper_.

.. _virtualenvwrapper: http://www.doughellmann.com/docs/virtualenvwrapper/

::

    git clone git://github.com/rlr/django-gevent-socketio-redis-chat-example.git
    cd django-gevent-socketio-redis-chat-example
    pip install -r requirements.txt


-------
Running
-------

Start the gevent socketio server::

    cd chatproject
    ./manage.py run_gevent 9000

Then point your browser to http://localhost:9000/.


----
Bugs
----

* I have noticed weird things happen in cases where multiple clients are
  connecting at same time. Race conditions?

-------------
TODO/Wishlist
-------------

* Connected users list
* Chat rooms
* Private/1:1 chat
* Experiment posting messages outside of socket.io connection. This way we can
  limit the socket.io connection to pubsub messages and all blocking calls
  (to database, etc.) can be made in through the normal django/wsgi stack.
