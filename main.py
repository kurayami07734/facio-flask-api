from flask import Flask
from flask_socketio import SocketIO, emit
from flask_cors import CORS, cross_origin

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/", methods=["POST", "GET"])

def placeholder():
    pass


if __name__ == "__main__":
    socketio.run(app, port=8080, debug=True)