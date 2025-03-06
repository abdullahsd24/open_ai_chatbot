from flask import Flask, request, jsonify
from chatgpt_bot_api_controller import ChatGPTBotAPI

app = Flask(__name__)

# Initialize the ChatGPTBotAPI with OpenAI API key
openai_api_key = "Paste you openai api key here"
chatbot_api = ChatGPTBotAPI(openai_api_key)

@app.route('/prompt', methods=['POST'])
def create_prompt():
    """
    Endpoint to create a new prompt.
    """
    data = request.json
    if 'prompt' not in data:
        return jsonify({"error": "Prompt is required"})

    prompt = data['prompt']
    prompt_index = chatbot_api.create_prompt(prompt)
    return jsonify({"message": "Prompt created successfully", "prompt_index": prompt_index})

@app.route('/response/<int:prompt_index>', methods=['GET'])
def get_response(prompt_index):
    """
    Endpoint to get the ChatGPT bot's response for a given prompt index.
    """
    try:
        response = chatbot_api.get_response(prompt_index)
        return jsonify({"response": response})
    except ValueError as e:
        return jsonify({"error": str(e)})

@app.route('/prompt/<int:prompt_index>', methods=['PUT'])
def update_prompt(prompt_index):
    """
    Endpoint to update an existing prompt.
    """
    data = request.json
    if 'new_prompt' not in data:
        return jsonify({"error": "new_prompt is required"})

    new_prompt = data['new_prompt']
    try:
        chatbot_api.update_prompt(prompt_index, new_prompt)
        return jsonify({"message": "Prompt updated successfully"})
    except ValueError as e:
        return jsonify({"error": str(e)})

@app.route('/prompt/<int:prompt_index>', methods=['DELETE'])
def delete_prompt(prompt_index):
    """
    Endpoint to delete a prompt.
    """
    try:
        chatbot_api.delete_prompt(prompt_index)
        return jsonify({"message": "Prompt deleted successfully"})
    except ValueError as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)