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


@app.route("/currency_request/<amount>/<currency_from>/<currency_to>")
def currency_request(currency_from, currency_to, amount):
    request_url = 'https://open.er-api.com/v6/latest/' + currency_to
    r = requests.get(request_url)
    json = r.json()

    rate = json['rates'][currency_from]

    result = rate * int(amount)

    return render_template('conversion.html',
                           amount=amount,
                           rate=str(rate),
                           currency_from=currency_from,
                           currency_to=currency_to,
                           result=str(result)
                           )


@app.route("/available_currencies")
def available_currencies():
    r = requests.get('https://open.er-api.com/v6/latest/USD')
    json = r.json()

    return render_template('available_currencies.html', currencies=json['rates'].keys())


if __name__ == '__main__':
    app.run(debug=True)
