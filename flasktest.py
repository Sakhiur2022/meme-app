from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
	return "Hi, you are not supposed to see this file. Go Away"
app.run(host = "0.0.0.0", port = "80")

