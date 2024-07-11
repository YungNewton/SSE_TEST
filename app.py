import logging
import eventlet

# Configure logging before monkey-patching
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Now monkey-patch with eventlet
eventlet.monkey_patch()

from flask import Flask
from flask_socketio import SocketIO
import time

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return "WebSocket server is running!"

def send_message():
    while True:
        socketio.emit('message', {'data': 'Hello, client!'})
        logger.debug('Sent message to client')  # Add logging
        time.sleep(1)

@socketio.on('connect')
def handle_connect():
    logger.info('Client connected')
    socketio.start_background_task(target=send_message)

@socketio.on('disconnect')
def handle_disconnect():
    logger.info('Client disconnected')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
