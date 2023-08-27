from flask import Flask, jsonify, request, send_from_directory
from chat_gpt import chat_gpt 



message_maker = chat_gpt.Message_Maker("system", "user")
manager = chat_gpt.API_Manager()

app = Flask(__name__, static_url_path='')

@app.route('/')
def serve_html():
    return send_from_directory('static', 'index.html')

@app.route('/api/data', methods=['POST'])
def get_data():
    data = request.json
    promp_message = data['key1']
    prompt = message_maker.make_user_message(promp_message)
    resp = manager.prompt(prompt)
    message = f"chatgpt: {resp[0]['content']}"
    print()
    return jsonify({"status": "Data received!", "received_data": message})


if __name__ == '__main__':
    app.run(debug=True)
