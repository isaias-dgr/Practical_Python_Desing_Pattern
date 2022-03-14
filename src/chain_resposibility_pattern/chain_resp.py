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


class EndHandler:
    def __init__(self) -> None:
        pass

    def handle_request(self, request, response):
        return response.encode('utf-8')


class AuthorizationHandler:
    def __init__(self) -> None:
        pass

    def handle_request(self, request, response):
        authorization_header = request["HTTP_AUTHORIZATION"]
        header_array = authorization_header.split()
        encoded_string = header_array[1]
        decoded_string = base64.b64decode(encoded_string).decode('utf-8')
        username, password = decoded_string.split(":")
        request["username"] = username
        request["password"] = password
        return self.next_handler.handler_request(request, response)


class UserHandler:

    def __init__(self) -> None:
        pass

    def handle_request(self, request, response=None):
        user = User.get_verified_user(request["username"], request["password"])
        request["user"] = user

        return self.next_handler.handler_request(request, response)


class PathHandler:

    def __init__(self) -> None:
        pass

    def handle_request(self, request, response=None):
        path = request["PATH_INFO"].split("/")
        name = request["user"].name
        if "goodbye" in path:
            response = f"Googbye {name}"
        else:
            response = f"Hello {name}"

        return self.next_handler.handler_request(request, response)


class Dispatcher:

    def __init__(self, handlers=[]):
        self.handlers = handlers

    def handler_request(self, request):
        for handler in self.handlers:
            request = handler(request)

        return request


def application(env, start_response):
    head = AuthorizationHandler()
    current = head
    current.next_handler = UserHandler()

    current = current.next_handler
    current.next_handler = PathHandler()

    start_response('200 OK', [('Content-Type', 'text/html')])
    return [head.handle_request(env)]
