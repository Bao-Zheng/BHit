from flask import Flask
from waitress  import serve

app = Flask(__name__)
@app.route("/",methods=["POST",])
def hello():
    return "hello!"

app.run(port=800)