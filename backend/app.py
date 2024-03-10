from flask import Flask,jsonify
from flask_cors import CORS

import json

app = Flask(__name__)
CORS(app)


@app.route('/')
def root():
    return "Hello World from Flask"


@app.route('/api/get_info')
def get_info():
    value = {
        "name": "Rafael",
        "lastname": "Mosquera",
        "socialMedia":
        {
            "facebookUser": "rafamosmad",
            "instagramUser": "rafamosmad",
            "xUser": "rafamosmad",
            "linkedin": "rafamosmada",
            "githubUser": "rafamosmad"
        },
        "blog": "https://rafamosmad.com",
        "author": "Rafael Mosquera"
    }

    return json.dumps(value)

# if __name__ == '__main__':
#     app.run()