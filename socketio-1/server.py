from aiohttp import web
import socketio
import time
import sys

# creates a new Async Socket IO Server
sio = socketio.AsyncServer()
# Creates a new Aiohttp Web Application
app = web.Application()
# Binds our Socket.IO server to our Web App
# instance
sio.attach(app)

# we can define aiohttp endpoints just as we normally
# would with no change


async def index(request):
    with open('index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')

# If we wanted to create a new websocket endpoint,
# use this decorator, passing in the name of the
# event we wish to listen out for


@sio.on('message')
async def print_message(sid, message):
    # When we receive a new event of type
    # 'message' through a socket.io connection
    # we print the socket ID and the message
    print("Socket ID: ", sid)
    print(message)
    try:
        last_loop_time = time.time()
        while True:
            if time.time() - last_loop_time > 0.5:
                await sio.emit('hello', data=('Hello',  'slave', 'master'))
                last_loop_time = time.time()
    except KeyboardInterrupt:
        print('interrupted!')


# We bind our aiohttp endpoint to our app
# router
app.router.add_get('/', index)

# We kick off our server
if __name__ == '__main__':
    port = sys.argv[1] if len(sys.argv) > 1 else 3000
    print(port)
    web.run_app(app, port=int(port))
