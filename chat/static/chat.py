from browser import document

# associe une fonction à l'événement "click" sur le bouton
firstname = document.query['firstname']
lastname = document.query['lastname']


async def connect():
    print('connected')


async def disconnect():
    print('disconnected from server')


def get_messages(messages):
    print(messages)


async def start_server():
    port = sys.argv[1] if len(sys.argv) > 1 else 3000
