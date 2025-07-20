from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    data = request.json
    print("Event received:", data)
    return {"message": "Event processed!"}, 200