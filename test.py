import socketio

sio = socketio.Client()

@sio.event
def connect():
    print('connection established')
    sio.emit('kate', 1770)

@sio.on('lmao')
def lmao(data):
    print('message received with ', data)

@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://127.0.0.1:5000/')
sio.wait()