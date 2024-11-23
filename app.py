from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_random_quote():
    response = requests.get("https://api.quotable.io/random", verify=False)
    if response.status_code == 200:
        return response.json()
    return {"content": "Error fetching quote.", "author": "Unknown"}

@app.route('/')
def index():
    quote = get_random_quote()
    return render_template("index.html", quote=quote)

if __name__ == '__main__':
    app.run(debug=True)
