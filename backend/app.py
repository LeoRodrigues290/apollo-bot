from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)  # Configurando o Socket.io

@app.route('/')
def index():
    return "Apollo Bot Backend Running"

if __name__ == '__main__':
    socketio.run(app, debug=True)

responses = {
    "Olá": "Olá! Como posso ajudar?",
    "Qual é o seu horário?": "Nosso horário é das 9h às 18h.",
    "Transferir": "Ok, vou transferir você para um operador humano."
}

@socketio.on('message')
def handle_message(msg):
    response = responses.get(msg, "Desculpe, não entendi.")
    socketio.emit('response', response)
