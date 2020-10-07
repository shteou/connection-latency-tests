#!/usr/bin/env python3
import numpy, requests, socket, ssl, sys, timeit

def print_percentile(a, p):
	result = numpy.percentile(a, p)
	print(f"\t{p}th percentile: {result}")

def print_percentiles(a):
	for p in [50, 90, 95, 99, 100]:
		print_percentile(a, p)

url = "https://stewartplatt.com/"
hostname = "stewartplatt.com"

def http_request():
	r = requests.get(url, stream=False)

s = requests.session()
def keepalive_request():
	r = s.get(url, stream=False)

def tcp_handshake():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((hostname, 443))

context = ssl.create_default_context()

def tls_handshake():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	with context.wrap_socket(s, server_hostname=hostname) as ssock:
		ssock.connect((hostname, 443))

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Usage:")
		print("  cxn.py [http] [keepalive] [tcp] [tls]")
		print("  e.g. ./cxn.py http keepalive")
		sys.exit(1)

	commands = sys.argv[1:]
	count = 10

	for c in commands:
		if "http" == c:
			print("HTTTP requests:")
			t = timeit.Timer('http_request()', setup='from __main__ import http_request')
			print_percentiles(t.repeat(repeat=count, number=1))
		elif "keepalive" == c:
			print("HTTP requests with keep-alive:")
			t = timeit.Timer('keepalive_request()', setup='from __main__ import keepalive_request')
			print_percentiles(t.repeat(repeat=count, number=1))
		elif "tcp" == c:
			print("TCP handshake requests:")
			t = timeit.Timer('tcp_handshake()', setup='from __main__ import tcp_handshake')
			print_percentiles(t.repeat(repeat=count, number=1))
		elif "tls" == c:
			print("TLS handshake requests:")
			t = timeit.Timer('tls_handshake()', setup='from __main__ import tls_handshake')
			print_percentiles(t.repeat(repeat=count, number=1))
		else:
			print(f"Warning! Invalid command: {c}")
