from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def greet():
    return "<h1> Greetings, programmer! </h1> "

if __name__ == '__main__':

    app.run(debug=True)