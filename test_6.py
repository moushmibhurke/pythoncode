import pytest
import requests
import json


def test_valid_login():
    url = 'https://reqres.in/api/login'
    data = {'email':'eve.holt@reqres.in','passward':'cityslicka'}
    responce = requests.get(url, data=data)
    token = json.loads(responce.text)
    assert responce.status_code == 200
    assert token[token] == "QpwL5tke4Pnpja7X4"
