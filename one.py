print("Hello, World!")

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    response_message = generate_response(user_message)
    return jsonify({'response': response_message})

def generate_response(message):
    # 簡單的回應邏輯，可以根據需要擴展
    if 'hello' in message.lower():
        return 'Hello! How can I help you today?'
    elif 'bye' in message.lower():
        return 'Goodbye! Have a nice day!'
    else:
        return 'I am not sure how to respond to that.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)