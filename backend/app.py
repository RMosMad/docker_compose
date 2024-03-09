from flask import Flask,jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/getMyInfo')
def getMyInfo():
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

    return jsonify(value)

if __name__ == '__main__':
    app.run(port=5000)