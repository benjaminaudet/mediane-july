import math
import random
from tkinter import *
from PIL import ImageTk
import PIL.Image
import asyncio
import socketio
import sys

sio = socketio.AsyncClient()


@sio.event
async def connect():
    print('connected')
    global root
    snake1 = Snake(root, 0, 0, 1)
    snake2 = Snake(root, 0, 0, 2)
    snake1.tick()
    snake2.tick()
    root.mainloop()


@sio.event
async def disconnect():
    print('disconnected from server')


@sio.event
def hello(a, b, c):
    print(a, b, c)


async def start_server():
    port = sys.argv[1] if len(sys.argv) > 1 else 3000
    await sio.connect('http://localhost:{}'.format(port), auth={'token': 'my-token'})
    await sio.emit('message', 'Hello world')
    await sio.wait()


SIZE = 20

if __name__ == '__main__':
    asyncio.run(start_server())
