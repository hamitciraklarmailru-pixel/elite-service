from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Google ve diğer arama motorlarının siteyi taramasına izin veren route
@app.route('/robots.txt')
def robots():
    return "User-agent: *\nAllow: /", 200, {'Content-Type': 'text/plain'}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/booking")
def booking():
    return render_template("booking.html")

if __name__ == "__main__":
    app.run(debug=True)
