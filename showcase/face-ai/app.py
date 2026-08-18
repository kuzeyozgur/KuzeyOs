from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def index():
    return jsonify({
        "project": "KuzeyOS",
        "module": "Face AI Showcase",
        "status": "demo"
    })

@app.get("/api/status")
def status():
    return jsonify({
        "camera": "demo",
        "recognition": "enabled",
        "detector": "YuNet",
        "recognizer": "SFace"
    })

@app.get("/api/people")
def people():
    return jsonify([
        {
            "name": "Demo User",
            "source": "synthetic"
        }
    ])

@app.get("/api/recognition-example")
def recognition_example():
    return jsonify({
        "event": "person.detected",
        "person": "Demo User",
        "confidence": 0.93,
        "synthetic": True
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
