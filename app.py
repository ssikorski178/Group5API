##Project 3
##REST API
## app.py

from flask import Flask
app = Flask(__name__)

@app.route("/")
def howdy():
    return "<h1>Hello World</h1>"

@app.route("/md5/<string>")
def md5():
    return

@app.route("/factorial/<int>")
def fact():
    return

@app.route("/fibonacci/<int>")
def fib():
    return

@app.route("/is-prime/<int>")
def prime():
	return

@app.route("/slack-alert/<string>")
def slackAlert():
	return

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')