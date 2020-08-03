from flask import Flask
from flask_cors import CORS
from flask import request,jsonify

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import detect_words

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    video_id = request.headers.get('video_id')
    input_sentence = request.headers.get('input_sentence')

    # first time the words appear in the video
    response = detect_words(video_id, input_sentence)

    return jsonify(response)

if __name__ == '__main__':
    print("RUNNING")
    app.run(host='localhost', port=5000)