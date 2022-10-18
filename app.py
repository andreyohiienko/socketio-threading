from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, async_mode="threading", engineio_logger=True)


@app.route("/")
def root():
    return "root"


@socketio.on("connect")
def connect():
    print("connect")


if __name__ == "__main__":
    socketio.run(app, debug=True)
