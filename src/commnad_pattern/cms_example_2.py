from ast import Mult
from decimal import InvalidOperation
from re import L


class AddCommnad:

    def __init__(self, receiver, value):
        self.receiver = receiver
        self.value = value

    def execute(self):
        self.receiver.add(self.value)

    def undo(self):
        self.receiver.subtract(self.value)


class SubstractCommnad:

    def __init__(self, receiver, value):
        self.receiver = receiver
        self.value = value

    def execute(self):
        self.receiver.subtract(self.value)

    def undo(self):
        self.receiver.add(self.value)


class MultiplyCommnad:

    def __init__(self, receiver, value):
        self.receiver = receiver
        self.value = value

    def execute(self):
        self.receiver.multiply(self.value)

    def undo(self):
        self.receiver.divide(self.value)


class DivideCommnad:

    def __init__(self, receiver, value):
        self.receiver = receiver
        self.value = value

    def execute(self):
        self.receiver.divide(self.value)

    def undo(self):
        self.receiver.multiply(self.value)


class CalculationInvoker:

    def __init__(self):
        self.commands = []
        self.undo_stack = []

    def add_new_command(self, command):
        self.commands.append(command)

    def run(self):
        for command in self.commands:
            command.execute()
            self.undo_stack.append(command)

    def undo(self):
        undo_command = self.undo_stack.pop()
        undo_command.undo()


class Accumulator:

    def __init__(self, value):
        self._value = value

    def add(self, value):
        self._value += value

    def subtract(self, value):
        self._value -= value

    def multiply(self, value):
        self._value *= value

    def divide(self, value):
        self._value /= value

    def __str__(self):
        return f"Current Value {self._value}"


if __name__ == "__main__":
    acc = Accumulator(10.0)

    invoker = CalculationInvoker()
    invoker.add_new_command(AddCommnad(acc, 12))
    invoker.add_new_command(SubstractCommnad(acc, 11))
    invoker.add_new_command(MultiplyCommnad(acc, 12))
    invoker.add_new_command(DivideCommnad(acc, 14))
    invoker.run()

    print(f"Res {acc}")

    invoker.undo()
    invoker.undo()
    invoker.undo()
    invoker.undo()

    print(f"Res undo {acc}")
