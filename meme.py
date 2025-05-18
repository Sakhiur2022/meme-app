from flask import Flask,render_template
import requests
import json

def getMeme():
	url = "https://meme-api.com/gimme"
	response = json.loads(requests.request("GET",url).text)
	meme_large = response["preview"][-2]
	subreddit = response["subreddit"]
	return meme_large,subreddit


app = Flask(__name__)
@app.route("/")
def index():
	meme_pic,subreddit = getMeme()
	return render_template("index.html",subreddit = subreddit, meme_pic = meme_pic)
app.run(host = "0.0.0.0", port="80")

