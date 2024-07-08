from flask import Flask, request
import time

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Flask API is up and running"

@app.route("/format/<str_2_format>", methods=['GET'])
def format_str(str_2_format:str):
    time.sleep(1)
    return (" ********** %s **********"% str_2_format)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
