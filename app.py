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
    <!DOCTYPE html>
    <html>
      <head>
        <meta charset="UTF-8" />
        <title>Viada OpenShift Bootcamp</title>
        <style>
          body {{
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
          }}
          .container {{
            background: #ffffff;
            border-radius: 8px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            max-width: 600px;
            width: 90%;
            padding: 20px;
          }}
          h1 {{
            text-align: center;
            color: #333;
            border-bottom: 2px solid #eee;
            padding-bottom: 10px;
            margin-bottom: 20px;
          }}
          p {{
            font-size: 16px;
            line-height: 1.5;
            margin: 10px 0;
            color: #555;
          }}
          p strong {{
            color: #333;
          }}
        </style>
      </head>
      <body>
        <div class="container">
          <h1>Welcome to the Viada OpenShift Bootcamp!</h1>
          <p><strong>Name:</strong> {name}</p>
          <p><strong>Role:</strong> {role}</p>
          <p><strong>Message:</strong> {message}</p>
        </div>
      </body>
    </html>
    """

if __name__ == '__main__':
    # Start the Flask server on port 8080
    app.run(host='0.0.0.0', port=8080)
