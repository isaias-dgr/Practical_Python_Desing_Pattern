from abc import ABCMeta, abstractclassmethod, abstractmethod
import random
import unittest


class Visitable:

    def accept(self, visitor):
        visitor.visit(self)


class CompositeVisitable(Visitable):

    def __init__(self, iterable) -> None:
        self.iterable = iterable

    def accept(self, visitor):
        for element in self.iterable:
            element.accept(visitor)

        visitor.visit(self)


class AbstractVisitor:
    __metaclass__ = ABCMeta

    @abstractmethod
    def visit(self, element):
        raise NotImplementedError("A visitor needs to define a visit method")


class Light(Visitable):
    def __init__(self, name) -> None:
        self.name = name
        self.status = self.get_status()

    def get_status(self):
        return random.choice(range(-1, 2))

    def is_online(self):
        return self.get_status() != -1

    def boot_up(self):
        self.status = 0


class LightStatusUpdateVisitor(AbstractVisitor):
    def __init__(self, person_1_home, person_2_home) -> None:
        self.person_1_home = person_1_home
        self.person_2_home = person_2_home

    def visit(self, element):
        if self.person_1_home:
            if self.person_2_home:
                element.status = 1
            else:
                element.status = 0
        elif self.person_2_home:
            element.status = 1
        else:
            element.status = 0


class Thermostat(Visitable):

    def __init__(self, name) -> None:
        self.name = name
        self.status = self.get_status()

    def get_status(self):
        temp_range = [x for x in range(-10, 31)]
        temp_range.append(None)
        return random.choice(temp_range)

    def is_online(self):
        return self.get_status() is not None

    def boot_up(self):
        pass


class ThermostatStatusUpdateVisitor(AbstractVisitor):
    def __init__(self, person_1_home, person_2_home) -> None:
        self.person_1_home = person_1_home
        self.person_2_home = person_2_home

    def visit(self, element):
        pass


class TemperatureRegulator(Visitable):
    def __init__(self, name) -> None:
        self.name = name
        self.status = self.get_status()

    def get_status(self):
        return random.choice(["heating", "cooling", "on", "off", "error"])

    def is_online(self):
        return self.get_status() != "error"

    def boot_up(self):
        self.status = "on"


class TemperatureRegulatorStatusUpdateVisitor(AbstractVisitor):
    def __init__(self, person_1_home, person_2_home) -> None:
        self.person_1_home = person_1_home
        self.person_2_home = person_2_home

    def visit(self, element):
        if self.person_1_home:
            if self.person_2_home:
                element.status = "on"
            else:
                element.status = "heating"
        elif self.person_2_home:
            element.status = "cooling"
        else:
            element.status = "off"


class DoorLock(Visitable):
    def __init__(self, name) -> None:
        self.name = name
        self.status = self.get_status()

    def get_status(self):
        return random.choice(range(-1, 2))

    def is_online(self):
        return self.get_status() != -1

    def boot_up(self):
        pass


class DoorLockStatusUpdateVisitor(AbstractVisitor):
    def __init__(self, person_1_home, person_2_home) -> None:
        self.person_1_home = person_1_home
        self.person_2_home = person_2_home

    def visist(self, element):
        if self.person_1_home:
            if self.person_2_home:
                element.status = 1
        elif self.person_2_home:
            element.status = 1
        else:
            element.status = 0


class CoffeeMachine(Visitable):
    def __init__(self, name) -> None:
        self.name = name
        self.status = self.get_status()

    def get_status(self):
        return random.choice(range(-1, 5))

    def is_online(self):
        return self.get_status() != -1

    def boot_up(self):
        self.status = 1


class CoffeeMachineStatusUpdateVisitor(AbstractVisitor):

    def __init__(self, person_1_home, person_2_home) -> None:
        self.person_1_home = person_1_home
        self.person_2_home = person_2_home

    def visit(self, element):
        if self.person_1_home:
            if self.person_2_home:
                element.status = 2
            else:
                element.status = 3
        elif self.person_2_home:
            element.status = 4
        else:
            element.status = 0


class Clock(Visitable):

    def __init__(self, name) -> None:
        self.name = name
        self.status = self.get_status()

    def get_status(self):
        return f"{random.randrange(24)}:{random.randrange(60)}"

    def is_online(self):
        return True

    def boot_up(self):
        self.status = "00:00"


class ClockStatusUpdateVisitor(AbstractVisitor):
    def __init__(self, person_1_home, person_2_home) -> None:
        self.person_1_home = person_1_home
        self.person_2_home = person_2_home

    def visit(self, element):
        if self.person_1_home:
            if self.person_2_home:
                pass
            else:
                element.status = "00:01"
        elif self.person_2_home:
            element.status = "20:22"
        else:
            pass


class CompositeVisitor(AbstractVisitor):
    def __init__(self, person_1_home, person_2_home) -> None:
        self.person_1_home = person_1_home
        self.person_2_home = person_2_home

    def visit(self, element):
        try:
            c = eval(f"{element.__class__.__name__} StatusUpdatecisitor")
        except:
            print(f"Visitor for {element.__class__.__name__} not found")
        else:
            visitor = c(self.person_1_home, self.person_2_home)
            visitor.visit(element)


class MyHomeSystem(CompositeVisitable):
    pass


class MyHomeSystemStatusUpdateVisitor(AbstractVisitor):
    def __init__(self, person_1_home, person_2_home) -> None:
        self.person_1_home = person_1_home
        self.person_2_home = person_2_home

    def visit(self, element):
        pass


class HomeAutomationBootTest(unittest.TestCase):

    def setUp(self):
        self.my_home_system = MyHomeSystem(
            [
                Thermostat("General Thermostat"),
                TemperatureRegulator("Thermal Regulator"),
                DoorLock("Front Door Lock"),
                CoffeeMachine("CoffeMachine"),
                Light("Bedroom Light"),
                Clock("System Clock"),
            ]
        )

    def test_person_1_not_home_person_2_not_home(self):
        expected_state = map(
            str,
            [
                self.my_home_system.iterable[0].status,
                'off',
                1,
                0,
                0,
                self.my_home_system.iterable[5].status
            ]
        )
        self.visitor = CompositeVisitor(False, False)
        self.my_home_system.accept(self.visitor)
        retrieved_state = sorted([str(x.status)
                                 for x in self.my_home_system.iterable])
        self.assertEqual(retrieved_state, sorted(expected_state))

    def test_person_1_home_person_2_not(self):
        expected_state = map(
            str,
            [
                self.my_home_system.iterable[0].status,
                'heating',
                0,
                3,
                0,
                "00:01"
            ]
        )
        self.visitor = CompositeVisitor(True, False)
        self.my_home_system.accept(self.visitor)
        retrieved_state = sorted([str(x.status)
                                  for x in self.my_home_system.iterable])
        self.assertEqual(retrieved_state, sorted(expected_state))

    def test_person_1_not_home_person_2_home(self):
        expected_state = map(
            str,
            [
                self.my_home_system.iterable[0].status,
                'cooling',
                1,
                4,
                1,
                "20:22",
            ]
        )
        self.visitor = CompositeVisitor(False, True)
        self.my_home_system.accept(self.visitor)
        retrieved_state = sorted([str(x.status)
                                 for x in self.my_home_system.iterable])
        self.assertEqual(retrieved_state, sorted(expected_state))

    def test_person_1_home_person_2_homt(self):
        expected_state = map(
            str,
            [
                self.my_home_system.iterable[0].status,
                'on',
                0,
                2,
                1,
                self.my_home_system.iterable[5].status,
            ]
        )
        self.visitor = CompositeVisitor(True, True)
        self.my_home_system.accept(self.visitor)
        retrieved_state = sorted([str(x.status)
                                 for x in self.my_home_system.iterable])
        self.assertEqual(retrieved_state, sorted(expected_state))


if __name__ == "__main__":
    unittest.main()
