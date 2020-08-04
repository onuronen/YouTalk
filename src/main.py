from flask import Flask
from flask_cors import CORS
from flask import request,jsonify
import os
import sys
sys.path.append(os.getcwd())
from src.utils import detect_words

def make_app():
    app = Flask(__name__)
    CORS(app)

    @app.route('/')
    def index():
        video_id = request.headers.get('video_id')
        input_sentence = request.headers.get('input_sentence')

        # first time the words appear in the video
        response = detect_words(video_id, input_sentence)
        return jsonify(response)

    return app
