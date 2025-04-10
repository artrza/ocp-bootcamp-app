#!/usr/bin/env python3
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    name = os.environ.get('NAME', 'NoName')
    role = os.environ.get('ROLE', 'NoRole')
    message = os.environ.get('MESSAGE', 'NoMessage')
    return f"""
    <html>
      <head><title>Viada OpenShift Bootcamp</title></head>
      <body>
        <h1>Welcome to the Viada OpenShift Bootcamp!</h1>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Role:</strong> {role}</p>
        <p><strong>Message:</strong> {message}</p>
      </body>
    </html>
    """

if __name__ == '__main__':
    # Starte den Flask-Server auf Port 8080
    app.run(host='0.0.0.0', port=8080)

