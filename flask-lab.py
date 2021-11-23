from flask import Flask, jsonify, render_template

app = Flask(__name__)


#
#
#
#
#
#
#

@app.route("currency_request")
def currency_request("get-currencies"):


    return "Implement."

@app.route("/")
def greet():
    return render_template('hello.html')


if __name__ == '__main__':
    app.run(debug=True)
