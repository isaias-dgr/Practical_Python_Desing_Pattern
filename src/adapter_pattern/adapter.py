class WhatIHave:
    def provided_function_1(self): print("What I Have func1")
    def provided_function_2(self): print("What I Have func2")


class WhatIWant:
    def required_function(self): pass


class MyAdapter(WhatIWant, WhatIHave):

    def __init__(self, what_i_have):
        self.what_i_have = what_i_have

    def provided_function_1(self):
        self.what_i_have.provided_function_1()

    def provided_function_2(self):
        self.what_i_have.provided_function_2()

    def required_function(self):
        print("required_function")
        self.provided_function_1()
        self.provided_function_2()


class ClientObject():

    def __init__(self, what_i_want):
        self.what_i_want = what_i_want

    def do_something(self):
        self.what_i_want.required_function()


if __name__ == "__main__":
    print("Adapter pattern")
    adaptee = WhatIHave()
    adapter = MyAdapter(adaptee)
    client = ClientObject(adapter)
    client.do_something()
