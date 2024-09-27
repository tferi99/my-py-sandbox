import asyncio
import socketio
import sys

if sys.platform == 'win32':
	asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

sio = socketio.AsyncClient()

@sio.event
async def connect():
    print('connection established')

@sio.event
async def my_message(data):
    print('message received with ', data)
    await sio.emit('my response', {'response': 'my response'})

@sio.on('general')
def on_message(data):
    print('GENERAL received:', data)

@sio.event
async def disconnect():
    print('disconnected from server')

async def connect_to_server():
    connected = False
    while not connected:
        try:
            await sio.connect('http://localhost:10000')
            connected = True
        except socketio.exceptions.ConnectionError:
            print("Connection failed, retrying in 5 seconds...")
            await asyncio.sleep(5)  # Wait before retrying

async def main():
    await connect_to_server()
    await sio.wait()

if __name__ == '__main__':
    asyncio.run(main())