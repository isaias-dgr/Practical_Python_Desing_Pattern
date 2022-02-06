class ObjectAdapter:
    def __init__(self, what_i_have):
        self.what_i_have = what_i_have

    def required_function(self):
        return self.what_i_have.provided_funtion_1()

    def __getattr__(self, attr):
        return getattr(self.what_i_have, attr)
