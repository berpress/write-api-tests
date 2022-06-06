# models
from faker import Faker

fake = Faker()


class RegisterUser:
    @staticmethod
    def random():
        username = fake.email()
        password = fake.password()
        return {"username": username, "password": password}
