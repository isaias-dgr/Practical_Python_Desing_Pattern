import base64


class User:

    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    @classmethod
    def get_verified_user(cls, username, password):
        return User(username, password, username, f"{username}@demo.com")


def get_user_object(username, password):
    return User.find_by_token(username, password)
