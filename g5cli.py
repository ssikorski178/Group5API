import argparse
import http
import requests

parser = argparse.ArgumentParser()

subparsers = parser.add_subparsers(help='commands')

#md5
md5_parser = subparsers.add_parser('md5', type=str, help='Returns a string as a json value')
md5_parser.add_argument('md5_string', action='store', help='Returns a string as a json value')

#factorial
fact_parser = subparsers.add_parser('factorial', type=int, help='Returns an integer as a factorial')
fact_parser.add_argument('fact_integer', action='store', help='Returns an integer as a factorial')

#fibonacci
fib_parser = subparsers.add_parser('fibonacci', type=int, help='Returns a specificed fibbonacci value')
fib_parser.add_argument('fib_integer', action='store', help='Returns a specificed fibbonacci value')

#is-prime
prime_parser = subparsers.add_parser('is-prime', type=int, help='Returns a true or false')
prime.add_argument('prime_integer', action='store', help='Returns a true or false')

args = parser.parse_args()
if args.md5_parser == 'md5'
	input_string = args.md5_string
	r=requests.get('http://127.0.0.1:5000/md5/'+string)
	print(r.text)
	
else if args.factorial_parses == 'factorial'
	input_int = args.fact_integer
	r=requests.get('http://127.0.0.1:5000/factorial/'+fact_integer)
	print(r.text)
	
else if args.fibonacci_parser == 'fibonacci'
	input_int = args.fib_integer
	r=requests.get('http://127.0.0.1:5000/factorial/'+fib_integer)
	print(r.text)

else if args.is-prime_parser == 'is-prime'
	input_int = args.prime_integer
	r=requests.get('http://127.0.0.1:5000/factorial/'+prime_integer)
	print(r.text)


