from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)


# Examples from slides
# r = requests.put('https://httpbin.org/put', data={'key': 'value'})
# r = requests.delete('https://httpbin.org/delete')
# r = requests.head('https://httpbin.org/get')
# r = requests.options('https://httpbin.org/get')
# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.get('https://httpbin.org/get', params=payload)


@app.route("/currency_request")
def currency_request():
    r = requests.get('https://open.er-api.com/v6/latest/USD')
    json = r.json()
    print(json)

    return json


@app.route("/")
def greet():
    return render_template('hello.html')


if __name__ == '__main__':
    app.run(debug=True)
