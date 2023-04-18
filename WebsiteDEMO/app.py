import os
import openai
from flask import Flask, request, render_template, make_response

app = Flask(__name__)

openai.api_key = "your api key"

prompt = "Tu trabajo es recomedar a el usuario el mejor platillo para sus gustos personales del menu"
messages = [{"role": "system", "content": prompt}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    ChatGPT_reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/chat", methods=["POST"])
def chat():
    user_input = request.json["prompt"]
    response_text = CustomChatGPT(user_input)
    decoded_text = response_text.strip()
    return make_response(decoded_text, 200)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

