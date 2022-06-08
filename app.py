from flask import Flask, render_template, request
from flask_socketio import SocketIO, send


PORT = 5000
SOCKETIP = '192.168.178.18'
#SOCKETIP = '94.212.51.78'


app = Flask(__name__)
app.config['SECRET_KEY'] = 'verysecret:)'
io = SocketIO(app)


@app.route('/')
def index():
    #socketio.emit('message', '[SERVER] Nog iemand kijkt mee 👀')
    return render_template('index.html', socket_url=f'ws://localhost:{PORT}' if request.remote_addr == '127.0.0.1' else f'ws://{SOCKETIP}:{PORT}')


@io.on('message')
def handle_message(msg):
    if msg == '':
        return
    
    print('Message:', msg)
    msg = msg.replace('<', '&lt').replace('>', '&gt')
    send(msg, broadcast=True)


if __name__ == '__main__':
    io.run(app, debug=True, host='0.0.0.0', port=PORT)
