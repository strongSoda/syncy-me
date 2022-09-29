# flask app setup and home api route

from flask import Flask, request, jsonify, send_file
from flask_cors import CORS

app = Flask(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# @app.route('/')
# def home():
#     return jsonify({'message': 'Hello World!'})


# render the index.html file
@app.route('/')
def index():
    # render the index.html file
    return send_file('index.html')





if __name__ == '__main__':
    app.run(debug=True)


