from flask import Flask, render_template
from flask.cli import load_dotenv
import os
from groq import Groq

app = Flask(__name__)

load_dotenv()
api_key = os.getenv("groq_api_key")

client = Groq(api_key="api_key")

@app.route("/")
def hello_world():
    return render_template("index.html")












if __name__ == "__main__":
    app.run(debug=True)