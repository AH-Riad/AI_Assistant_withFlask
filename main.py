from flask import Flask, jsonify, render_template, request
from flask.cli import load_dotenv
import os
from groq import Groq

app = Flask(__name__)

load_dotenv()
api_key = os.getenv("groq_api_key")

client = Groq(api_key=api_key)

@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    question = request.form.get('question')
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            { "role": "system", "content": "You are a helpful assistant." },
            {
                "role": "user",
                "content": question
            }],
            temperature = 0.7,
            max_tokens = 512
        
    )

    answer = response.choices[0].message.content.strip()

    return jsonify({
        "response": answer
    }),200


@app.route("/summarize", methods = ["POST"])
def summarize():
    email_text = request.form.get('email-text')
    prompt = f"Summarize the following email in a concise manner:\n\n{email_text}"
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            { "role": "system", "content": "You are an expert email assistant." },
            {
                "role": "user",
                "content": prompt
            }]
        ,
        temperature = 0.7,
        max_tokens = 512
    )

    summary = response.choices[0].message.content.strip()

    return jsonify({
        "response": summary
    }),200



if __name__ == "__main__":
    app.run(debug=True)