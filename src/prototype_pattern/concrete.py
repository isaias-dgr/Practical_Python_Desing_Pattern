from prototype_1 import Prototyope
from copy import deepcopy


class Concrete(Prototype):

    def clone(self):
        return deepcopy(self)
