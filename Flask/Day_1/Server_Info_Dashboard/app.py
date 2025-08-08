from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/")
def server_info():
    ip = request.remote_addr
    port = request.environ.get('SERVER_PORT')
    env = os.getenv("FLASK_ENV", "production")
    return f"<h3>Server Info</h3>IP: {ip}<br>Port: {port}<br>Environment: {env}"

@app.route("/status")
def status():
    if app.debug:
        return "Running in Debug Mode"
    return "Running in Production Mode"

if __name__ == "__main__":
    app.run(debug=True, port=8000) 
