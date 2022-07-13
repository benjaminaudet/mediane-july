from aiohttp import web
import socketio
import time
import sys
import json

sio = socketio.AsyncServer(cors_allowed_origins='*')
app = web.Application()
sio.attach(app)

app.add_routes([web.static('/static', './static')])

users = []
messages = []


async def index(request):
    with open('index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')


async def chat(request):
    firstname = request.rel_url.query.get('firstname', '')
    lastname = request.rel_url.query.get('lastname', '')
    print(users)
    if not firstname or not lastname:
        with open('index.html') as f:
            return web.Response(text=f.read(), content_type='text/html')
    new_user = {'firstname': firstname, 'lastname': lastname,
                'remote': request.remote}
    if not new_user in users:
        users.append(new_user)
    with open('chat.html') as f:
        return web.Response(text=f.read(), content_type='text/html')
app.add_routes([web.get('/', index)])
app.add_routes([web.get('/chat', chat)])


@sio.on('get_messages_request')
async def get_messages(sid):
    print(sid)
    return messages


@sio.on('send_message_request')
async def send_message(sid, data):
    messages.append({'message': data['message'], 'author': data['author']})
    await sio.emit('get_messages_response', data=messages)

if __name__ == '__main__':
    port = sys.argv[1] if len(sys.argv) > 1 else 3000
    web.run_app(app, port=int(port))
