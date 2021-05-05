import requests


def test_valid_api_token():
    response = requests.get("http://localhost/wp-json/anxapi/v1/up/?access_token=test_access_token")
    assert response.status_code == 200
    assert response.text == "OK"

def test_invalid_api_token():
    response = requests.get("http://localhost/wp-json/anxapi/v1/up/?access_token=invalid_access_token")
    assert response.status_code == 401
    assert response.text == "You are not authorized to do this"
