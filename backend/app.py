from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app, cors_allowed_origins="*")

# Rota de teste para verificar o backend
@app.route('/')
def index():
    return jsonify({"message": "Apollo Bot Backend Running"})

# Evento para lidar com mensagens recebidas do frontend
@socketio.on('send_message')
def handle_message(data):
    message = data.get("message", "")
    response = generate_bot_response(message)
    emit('receive_message', {'sender': 'bot', 'text': response})


def generate_bot_response(message):
    responses = {
        "Olá": "Olá! Como posso ajudar?",
        "Qual é o seu horário?": "Nosso horário é das 9h às 18h.",
        "Transferir": "Ok, vou transferir você para um operador humano."
    }

    if message == "Transferir":
        # Aqui, podemos definir um fluxo para escalar o atendimento
        return "Aguarde um momento enquanto transferimos você para um operador humano."

    return responses.get(message, "Desculpe, não entendi. Você poderia reformular?")


if __name__ == '__main__':
    socketio.run(app, debug=True)
