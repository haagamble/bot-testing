from flask import Flask, request
from datetime import datetime
from random import choice
import json

# Declaring the flask app
app = Flask(__name__)

# opening JSON file (not Cyrillic)
with open('states.json') as f:
    # return JSON object as a dictionary
    data = json.load(f) 

# test iteration by printing something
for state in data['states']:
    print(state['name'])

# testing index
@app.route('/', methods=['GET'])
def index():
    return "<h1>Hello from TBot</h1>"

# for testing json_response
@app.route('/get_time')
def get_time():
    now = datetime.utcnow()
    return str(now)

# for testing json data
@app.route('/states', methods=['GET'])
def get_states():
    return str(data)

# testing dialogflow get request and send response
@app.route('/webhook', methods=['POST'])
def webhook():
    return {
        "fulfillmentText": "Hi from Heroku"
    }

if __name__ == '__main__':
    app.run(debug=True)
