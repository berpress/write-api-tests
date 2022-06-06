import requests


class TestRegistration:
    def test_registration(self):
        body = {"username": "test@test23.com", "password": "Password"}
        response = requests.post("https://stores-tests-api.herokuapp.com/register", json=body)
        assert response.status_code == 201
        assert response.json().get('message') == 'User created successfully.'
        assert response.json().get('uuid')
        assert isinstance(response.json().get('uuid'), int)
