from flask import Flask, request, jsonify
from backend.mental_health_companion import MentalHealthCompanion
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
companion = MentalHealthCompanion()

@app.route('/api/assess', methods=['POST'])
def mental_health_assessment():
    input_text = request.json['input']
    assessment = companion.assess_mental_health(input_text)
    return jsonify({'assessment': assessment})

@app.route('/api/chat', methods=['POST'])
def emotional_support_chatbot():
    input_text = request.json['input']
    response = companion.chat_emotional_support(input_text)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
