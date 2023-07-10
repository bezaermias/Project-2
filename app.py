from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':               # this should always be at the end
    app.run(debug=True, host="0.0.0.0")