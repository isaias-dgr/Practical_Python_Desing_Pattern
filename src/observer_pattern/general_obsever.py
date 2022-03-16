from subprocess import call


class ConcreteObserver:

    def update(self, observerd):
        print(f"Observing {observerd}")


class Observable:
    def __init__(self) -> None:
        self.callbacks = set()

    def register(self, callback):
        self.callbacks.add(callback)

    def unregister(self, callback):
        self.callbacks.discard(callback)

    def unregister_all(self, callback):
        self.callbacks = set()

    def update_all(self):
        for callback in self.callbacks:
            callback(self)


def main():

    observed = Observable()
    observer1 = ConcreteObserver()

    observed.register(lambda x: observer1.update(x))

    observed.update_all()


if __name__ == "__main__":
    main()
