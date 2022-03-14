import pprint
import base64
from user_handler import User

pp = pprint.PrettyPrinter(indent=4)


def application(env, start_response):
    authorization_header = env["HTTP_AUTHORIZATION"]
    header_array = authorization_header.split()
    encode_string = header_array[1]
    decode_string = base64.b64decode(encode_string).decode('utf-8')
    username, password = decode_string.split(":")

    user = User.get_verified_user(username, password)
    start_response('200 OK', [('Content-Type', 'text/html')])
    response = f"Hello {user.name}!"

    path = env["PATH_INFO"].split("/")

    if "goodbye" in path:
        response = f"Googbye {user.name}"
    else:
        response = f"Hello {user.name}"

    return [response.encode('utf-8')]
