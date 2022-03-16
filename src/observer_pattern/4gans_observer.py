from abc import ABCMeta, abstractmethod


class Observer:
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self, observed): pass


class ConcreteObserver(Observer):

    def update(self, observer):
        print(f"Observing: {observer}")


class Observable:

    def __init__(self) -> None:
        self.observed = set()

    def register(self, observer):
        self.observers.add(observer)

    def unregister(self, observer):
        self.observers.discard(observer)

    def unregister_all(self):
        self.observers = set()

    def update_all(self):
        for observer in self.observers:
            observer.update(self)
