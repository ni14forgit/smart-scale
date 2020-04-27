# import socketio

# sio = socketio.Client()

# @sio.event
# def connect():
#     print('connection established')
#     sio.emit('kate', 1770)

# @sio.on('lmao')
# def lmao(data):
#     print('message received with ', data)

# @sio.event
# def disconnect():
#     print('disconnected from server')

# sio.connect('http://192.168.1.13:5000/')
# sio.wait()

from socketIO_client import SocketIO, LoggingNamespace

def on_bbb_response(*args):
    print('on_bbb_response', args)

with SocketIO("http://192.168.1.13", 5000, LoggingNamespace) as socketIO:
    socketIO.emit('kate', 2070)
    socketIO.wait_for_callbacks(seconds=1)

