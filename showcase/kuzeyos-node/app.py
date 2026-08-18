from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.get("/")
def index():
    try:
        return render_template("dashboard.html")
    except Exception:
        return jsonify({
            "project": "KuzeyOS",
            "module": "KuzeyOS Node Showcase",
            "status": "demo"
        })

@app.get("/api/status")
def status():
    return jsonify({
        "status": "online",
        "mode": "showcase",
        "face_ai": "demo",
        "automation": "demo"
    })

@app.get("/api/events")
def events():
    return jsonify([
        {
            "type": "person.detected",
            "source": "face-ai",
            "person": "Demo User",
            "timestamp": "2026-01-01T12:00:00Z"
        }
    ])

@app.get("/api/devices")
def devices():
    return jsonify([
        {
            "id": "demo-light",
            "name": "Demo Light",
            "type": "light",
            "room": "demo-room",
            "state": "off"
        },
        {
            "id": "demo-climate",
            "name": "Demo Climate",
            "type": "climate",
            "room": "demo-room",
            "state": "idle"
        }
    ])

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=False)
