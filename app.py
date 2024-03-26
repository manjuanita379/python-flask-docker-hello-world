from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"


if __name__ == "__master__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='54.151.2.1',port=5000)
