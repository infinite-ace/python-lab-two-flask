import requests
from behave import *
use_step_matcher("re")

@given('we have a valid api url')
def check_url(context):
    try:
        response = requests.get('https://open.er-api.com/v6/latest/USD')
        pass
        print("URL is VALID and exists on the internet")
    except requests.ConnectionError as exception:
        assert True is False
        print("URL is INVALID and does not exist on Internet")


