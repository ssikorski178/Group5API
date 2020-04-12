##Project 3
##REST API
## app.py

from flask import Flask, jsonify
import hashlib
app = Flask(__name__)

@app.route("/")
def howdy():
    return "<h1>Howdy and welcome to our container application!</h1>"

@app.route("/md5/<string>")
def md5(string):
	hash_object = hashlib.md5(string.encode())
	md5_hash = hash_object.hexdigest()
	return jsonify(md5_hash)
    
@app.route("/factorial/<num>")
def fact(num):
	intnum = int(num)
	factorial = 1
	if intnum == 0:
		return jsonify('Factorial of 0 is 1')
	if intnum < 0:
		return jsonify('Error, please enter a positive integer')
	else:
		for i in range(1,intnum + 1):
			factorial = factorial*i
		return jsonify(str(factorial))
    

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
def slackAlert():
	return

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
