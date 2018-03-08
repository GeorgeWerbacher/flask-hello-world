#import the Flask class from the flask module
from flask import Flask

# create the application object
app = Flask(__name__)

# error handling
app.config["DEBUG"] = True

# use the decorator patterns to link the view to a url
@app.route("/")
@app.route("/hello")

# define the view using a function, which returns a string
def hello_world():
	return "Hello, World!?!?!?!"

# dynamic Route
@app.route("/test/<search_query>")
def search(search_query):
	return search_query

# Flask Converters
@app.route("/integer/<int:value>")
def int_type(value):
	print(value + 1)
	return "correct"

@app.route("/float/<float:value>")
def float_type(value):
	print (value + 1)
	return "correct"

# Dynamic Route that Accepts Slashes
@app.route("/path/<path:value>")
def path_type(value):
	print(value)
	return "correct"


# dynamic route with explicit status code
@app.route("/name/<name>")
def index(name):
	if name.lower() == "michael":
		return "Hello {}".format(name)
	else:
		return "Not Found", 404

# stat the developement server using the run() method
if __name__ == "__main__":
	app.run()