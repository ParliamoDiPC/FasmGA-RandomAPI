from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def main():
	return "<!DOCTYPE html><html><head><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"><link rel=\"stylesheet\" href=\"https://cdn.jsdelivr.net/npm/water.css@2/out/water.css\"></head><body><h1>Fasm.ga Random APIs</h1><hr><h3>Number APIs</h3><p><code>/numbers/random?min=&max=</code>: random number generator, where min is the minimum number and max is the maxinum number<br></p><h3>Text APIs</h3><p><code>/text/url_encode?text=</code>: url format encoder, where text is the text to encode<br><code>/text/url_decode?text=</code>: url format decoder, where text is the text to decode</p><h3>Hashing APIs</h3><p><code>/hash/sha1?text=</code>: SHA1 hash generator, where text is the text to hash<br><code>/hash/sha256?text=</code>: SHA256 hash generator, where text is the text to hash<br><code>/hash/sha512?text=</code>: SHA512 hash generator, where text is the text to hash<br></body></html>"

@app.route("/numbers/random")
def numbers_random():
	if not request.args.get("min"): return "[err] No \"min\" value"
	if not request.args.get("max"): return "[err] No \"max\" value"
	try:
		import random
		return str(random.randint(int(request.args.get("min")), int(request.args.get("max"))))
	except:
		return "[err] \"min\" or \"max\" is not an int, or min value is major of max value"

@app.route("/numbers/multiply")
def numbers_multiply():
	if not request.args.get("min"): return "[err] No \"min\" value"
	if not request.args.get("max"): return "[err] No \"max\" value"
	try:
		import random
		return str(random.randint(int(request.args.get("min")), int(request.args.get("max"))))
	except:
		return "[err] "

@app.route("/text/url_encode")
def url_encode():
	import urllib
	if not request.args.get("text"): return "[err] No \"text\" value"
	return urllib.parse.quote(request.args.get("text"))

@app.route("/text/url_decode")
def url_decode():
	import urllib
	if not request.args.get("text"): return "[err] No \"text\" value"
	return urllib.parse.unquote(request.args.get("text"))

@app.route("/hash/sha1")
def hash_sha1():
	import hashlib
	if not request.args.get("text"): return "[err] No \"text\" value"
	return hashlib.sha1(request.args.get("text").encode()).hexdigest()

@app.route("/hash/sha256")
def hash_sha256():
	import hashlib
	if not request.args.get("text"): return "[err] No \"text\" value"
	return hashlib.sha256(request.args.get("text").encode()).hexdigest()

@app.route("/hash/sha512")
def hash_sha512():
	import hashlib
	if not request.args.get("text"): return "[err] No \"text\" value"
	return hashlib.sha512(request.args.get("text").encode()).hexdigest()

@app.errorhandler(404)
def error_404(error):
	return "<!DOCTYPE html><html><head><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"><link rel=\"stylesheet\" href=\"https://cdn.jsdelivr.net/npm/water.css@2/out/water.css\"></head><body><h1>Error 404</h1><hr><p>Page not found.</p></body></html>"

app.run("0.0.0.0")