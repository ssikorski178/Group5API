import argparse
import http
import requests

parser = argparse.ArgumentParser()

subparsers = parser.add_subparsers(help='commands', dest='cli')

#md5
md5_parser = subparsers.add_parser('md5', help='Returns a string as a json value')
md5_parser.add_argument('md5_string', action='store', help='Returns a string as a json value')

#factorial
fact_parser = subparsers.add_parser('factorial', help='Returns an integer as a factorial')
fact_parser.add_argument('fact_integer', action='store', help='Returns an integer as a factorial')

#fibonacci
fib_parser = subparsers.add_parser('fibonacci', help='Returns a specificed fibbonacci value')
fib_parser.add_argument('fib_integer', action='store', help='Returns a specificed fibbonacci value')

#is-prime
prime_parser = subparsers.add_parser('is-prime', help='Returns a true or false')
prime_parser.add_argument('prime_integer', action='store', help='Returns a true or false')

args = parser.parse_args()
if args.cli == 'md5':
	input_md5string = args.md5_string
	r=requests.get('http://127.0.0.1:5000/md5/'+input_md5string)
	print(r.text)
	
if args.cli == 'factorial':
	input_factint = args.fact_integer
	r=requests.get('http://127.0.0.1:5000/factorial/'+input_factint)
	print(r.text)
	
if args.cli == 'fibonacci':
	input_fibint = args.fib_integer
	r=requests.get('http://127.0.0.1:5000/fibonacci/'+input_fibint)
	print(r.text)

if args.cli == 'is-prime':
	input_primeint = args.prime_integer
	r=requests.get('http://127.0.0.1:5000/is-prime/'+input_primeint)
	print(r.text)


