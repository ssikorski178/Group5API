##Project 3
##REST API
## app.py

from flask import Flask, jsonify
import hashlib
from slackclient import SlackClient

app = Flask(__name__)

@app.route("/")
def howdy():
    return "<h1>Howdy and welcome to our container application!</h1>"

@app.route("/md5/<string>")
def md5(string):
	hash_object = hashlib.md5(string.encode())
	md5_hash = hash_object.hexdigest()
	return jsonify(
		input = string,
		output =md5_hash)
    
@app.route("/factorial/<num>")
def fact(num):
	intnum = int(num)
	factorial = 1
	if intnum == 0:
		return jsonify(
			input = num,
			output = int(1))
	if intnum < 0:
		return jsonify(
			input = num,
			output = 'Error, please enter a positive integer')
	else:
		for i in range(1,intnum + 1):
			factorial = factorial*i
		return jsonify(
			input = int(num),
			output = int(factorial))
    

@app.route('/fibonacci/<int(signed=True):x>')
def fibo(x):
    return jsonify(
        input = x,
        output = fib(x)
        )
def fib(n):
    if n < 0 :
        print ("Error, input needs to be positive.")   
    else:
        a, b = 0, 1
        array = [0]
        while b <= n:
            array.append(b)
            a, b = b, a+b   
    return array

@app.route('/is-prime/<int:x>')
def prime(x):
    return jsonify(
        input=x,
        output=is_prime(x)
        )
def is_prime(n):
   if n > 1:
       for i in range(2, n):
           if (n % i == 0):
               return False      
           else:
              return True
   else:
       return False

@app.route("/slack-alert/<string>")
##CHANNEL IDs:
### general - C2581UKGA
### test -- C011CNT49QX
def slackAlert(string):
  slack_client = SlackClient('xoxb-73266387591-1057780958419-cmZK7xvCKYb5sblKCEnyci2n')
  attempt_alert = slack_client.api_call("chat.postMessage",
    channel='C011CNT49QX',
    text=string,
    username='Group5-slack-alert')

  if attempt_alert.get('ok'):
    return jsonify(input=string, output=True)
  else:
    return jsonify(input=string, output=False)




if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
