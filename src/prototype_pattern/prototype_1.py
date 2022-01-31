from abc import ABCMeta, abstractclassmethod


class Prototype(metaclass=ABCMeta):

    @abstractclassmethod
    def clone(self):
        pass
