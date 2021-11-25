from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)


@app.route("/currency_request/<amount>/<currency_from>/<currency_to>")
def currency_request(currency_from, currency_to, amount):
    # Use case: Changing the url to invalid will invoke the except clause
    request_url = 'https://open.er-api.com/v6/latest/' + currency_to
    try:
        r = requests.get(request_url)
        json = r.json()
    except:
        print("Request failed. Try again later.")

    rate = json['rates'][currency_from]

    result = rate * int(amount)

    return render_template('conversion.html',
                           amount=amount,
                           rate=str(rate),
                           currency_from=currency_from,
                           currency_to=currency_to,
                           result=str(result)
                           )


# Reversed
@app.route("/reverse_currency_request/<amount>/<currency_from>/<currency_to>")
def reverse_currency_request(currency_from, currency_to, amount):
    # Use case: Changing the url to invalid will invoke the except clause
    request_url = 'https://open.er-api.com/v6/latest/' + currency_to
    try:
        r = requests.get(request_url)
        json = r.json()
    except:
        print("Request failed. Try again later.")

    rate = json['rates'][currency_from]

    # Creates black holes when uncommented.
    rate = 0

    result = ""
    try:
        result = 1 / rate * int(amount)
    except ZeroDivisionError:
        result = "You just created another black with the mighty technique of dividing by zero." \
                 " Please pick(carefully) another number to divide with."
        print("You just created another black with the mighty technique of dividing by zero."
              " Please pick(carefully) another number to divide with.")
        return render_template('request_failed.html', error_message="Division By Zero. Now that's really cool!")

    return render_template('conversion.html',
                           amount=amount,
                           rate=str(rate),
                           currency_from=currency_from,
                           currency_to=currency_to,
                           result=str(result)
                           )


@app.route("/currency_request_json/<amount>/<currency_from>/<currency_to>")
def currency_request_json(currency_from, currency_to, amount):
    # Use case: Changing the url to invalid will invoke the except clause
    request_url = 'https://open.er-api.com/v6/latest/' + currency_to

    try:
        r = requests.get(request_url)
        json = r.json()
    except:
        print("Request failed. Try again later or make sure your url is valid.")
        return jsonify("Bad request. The API may be down for maintenance or invalid url is passed. Check your request"
                       "url and validate through the browser, or try again later.")

    rate = json['rates'][currency_from]

    result = rate * int(amount)

    return jsonify(result)


@app.route("/")
def available_currencies():
    # Use case: Changing the url to invalid will invoke the except clause
    request_url = "https://open.er-api.com/v6/latest/USD"

    try:
        r = requests.get(request_url)
        json = r.json()
    except:
        print("Request failed. Try again later.")
        return render_template('request_failed.html', error_message="API URL is not valid or site is down"
                                                                    " for maintenance.")

    currencies = json['rates'].keys()
    currencies_list = []
    link_to_navigate = "https://localhost:5000/currency_request/<amount>/<currency_from>/<currency_to>"
    for currency in currencies:
        currencies_list.append(currency)

    return render_template('available_currencies.html', currencies=currencies_list)


if __name__ == '__main__':
    app.run(debug=True)
