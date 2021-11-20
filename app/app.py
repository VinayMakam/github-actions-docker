from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"


def print_ip():
    return socket.gethostbyname(socket.gethostname())


if __name__ == "__main__":
    app.run()
