from flask import Flask
from flask.cli import load_dotenv
import os
from groq import Groq

app = Flask(__name__)

load_dotenv()
api_key = os.getenv("groq_api_key")

client = Groq(api_key="api_key")

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"












if __name__ == "__main__":
    app.run(debug=True)