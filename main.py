import os
from flask import Flask, render_template, url_for

FLASK_KEY = os.environ.get("SECRET_KEY")

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')

@app.route('/')
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=False, port=5000)
