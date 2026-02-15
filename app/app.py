from flask import Flask, jsonify
import os
import socket
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
        return jsonify({
                    "message": "DevOps Demo App Running",
                            "hostname": socket.gethostname(),
                                    "timestamp": str(datetime.now())
                      })
@app.route("/health")
def health():
        return jsonify({"status": "healthy"}), 200

@app.route("/version")
def version():
        return jsonify({"version": "1.0.0"}), 200

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)

