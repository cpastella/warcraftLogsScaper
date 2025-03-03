from flask import Flask

app = Flask(__name__) 

@app.route("/", strict_slashes=False, methods=["GET"])
def index():
    return "<h1>This is the Home Page</h1>"