from register_3_step.api import Register
from register_3_step.models import RegisterUser
from schemas.registration import valid_schema

URL = "https://stores-tests-api.herokuapp.com"


class TestRegistration:
    def test_registration(self):
        body = RegisterUser.random()
        response = Register(url=URL).register_user(body=body, schema=valid_schema)
        assert response.status == 201
        assert response.response.get('message') == 'User created successfully.'
        assert response.response.get('uuid')
