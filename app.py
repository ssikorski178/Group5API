##Project 3
##REST API
## app.py

from flask import Flask, jsonify, requests
import hashlib
from slackclient import SlackClient
import math
import os
from redis imports Redis, RedisError

app = Flask(__name__)
redis = Redis(host="redis", socket_connect_timeout=2, socket_timeout=2)

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
    
@app.route("/factorial/<int:num>")
def fact(num):
	factorial = 1
	if isinstance(num, int) == True:
		if num == 0:
			return jsonify(
				input = num,
				output = int(1))
		if num < 0:
			return jsonify(
				input = num,
				output = 'Error, please enter a positive integer')
		else:
			for i in range(1,num + 1):
				factorial = factorial*i
			return jsonify(
				input = int(num),
				output = int(factorial))
	else:
		return jsonify(
				input = num,
				output = 'Error, please enter an integer')
    

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
   if n < 2 :
       return False
   if n % 2 == 0 and n > 2: 
        return False
   for i in range(3, int(math.sqrt(n)) + 1, 2):
       if n % i == 0:
           return False
   return True


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


@app.route('/keyval', methods=['POST', 'PUT'])
def key_value():
   
    json_value = {
        'key': None,
        'value': None,
        'command': 'CREATE' if request.method=='POST' else 'UPDATE',
        'result': False,
        'error': None
    }

    try:
        test_value = redis.get(json_value['key'])
    except RedisError:
        json_value['error'] = "Unable to connect to redis."
        return jsonify(json_value), 400

    if request.method == 'POST' and not test_value == None:
        json_value['error'] = "Unable to create new record becausse key already exists."
        return jsonify(json_value), 409

    elif request.method == 'PUT' and test_value == None:
        json_value['error'] = "Unable to update record because key does not exist."
        return jsonify(json_value), 404

    elif redis.set(json_value['key'], json_value['value']) == False:
        json_value['error'] = "There was a problem creating the value in Redis."
        return jsonify(json_value), 400
    else:
        json_value['result'] = True
        return jsonify(json_value), 200


@app.route('/keyval/<string:key>', methods=['GET', 'DELETE'])
def key_value_retrieve(key):
    json_value = {
        'key': key,
        'value': None,
        'command': "{} {}".format('RETRIEVE' if request.method=='GET' else 'DELETE', key),
        'result': False,
        'error': None
    }

    try:
        test_value = redis.get(key)
    except RedisError:
        json_value['error'] = "Unable to connect to redis."
        return jsonify(json_value), 400

    if test_value == None:
        json_value['error'] = "Key does not exist."
        return jsonify(json_value), 404
    else:
        json_value['value'] = test_value

    if request.method == 'GET':
        json_value['result'] = True
        return jsonify(json_value), 200

    elif request.method == 'DELETE':
        ret = redis.delete(key)
        if ret == 1:
            json_value['result'] = True
            return jsonify(json_value)
        else:
            json_value['error'] = f"Unable to delete key (expected return value 1; client returned {ret})"
            return jsonify(json_value), 400



if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
