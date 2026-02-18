from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"msg": "BCFM"})

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/post", methods=["POST"])
def post():
    body = request.get_json(silent=True) or {}
    key = body.get('key')
    value = body.get('value')
    return jsonify({"key": key, "value": value})

if __name__ == '__main__':
    app.run(port=8093)
    
