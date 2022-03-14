from asyncore import dispatcher


class Dispatcher:

    def __init__(self, handlers=[]):
        self.handlers = handlers

    def handle_request(self, request):
        for handle in self.handlers:
            request = handle(request)

        return request


def func_1(in_string):
    print(f"func_1 {in_string}")
    return "".join([x for x in in_string if x != '1'])


def func_2(in_string):
    print(f"func_2 {in_string}")
    return "".join([x for x in in_string if x != '2'])


def func_3(in_string):
    print(f"func_3 {in_string}")
    return "".join([x for x in in_string if x != '3'])


def func_4(in_string):
    print(f"func_4 {in_string}")
    return "".join([x for x in in_string if x != '4'])


def main(request):

    dispatcher = Dispatcher([
        func_1, func_2, func_3, func_4,
    ])

    return dispatcher.handle_request(request)


if __name__ == "__main__":
    res = main("1221345439")
    print(f"main {res}")
