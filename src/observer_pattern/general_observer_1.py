import time


class ConcreteObserver:

    def update(self, observerd):
        print(f"Observing {observerd}")


class Observable:
    def __init__(self) -> None:
        self.callbacks = set()
        self.changed = False

    def register(self, callback):
        self.callbacks.add(callback)

    def unregister(self, callback):
        self.callbacks.discard(callback)

    def unregister_all(self, callback):
        self.callbacks = set()

    def poll_for_changge(self):
        if self.changed:
            self.update_all

    def update_all(self):
        for callback in self.callbacks:
            callback(self)


def main():

    observed = Observable()
    observer1 = ConcreteObserver()

    observed.register(lambda x: observer1.update(x))

    while True:
        time.sleep(3)
        observed.poll_for_changge()


if __name__ == "__main__":
    main()
