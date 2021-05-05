import requests


def test_valid_api_token():
    response = requests.get("http://localhost/wp-json/anxapi/v1/modules/?access_token=test_access_token")
    assert response.status_code == 200

    data = response.json()
    assert data["runtime"]["platform"] == "php"
    assert data["runtime"]["framework"] == "wordpress"
    assert len(data["modules"]) > 0

def test_invalid_api_token():
    response = requests.get("http://localhost/wp-json/anxapi/v1/modules/?access_token=invalid_access_token")
    assert response.status_code == 401
    assert response.json() == {
        "code":"rest_unauthorized",
        "message":"You are not authorized to do this",
        "data":{
            "status":401
        }
    }
