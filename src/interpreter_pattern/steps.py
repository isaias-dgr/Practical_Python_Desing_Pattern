from aloe import *


@step(r'I have the number (\d+)')
def have_the_number(step, number):
    world.number = int(number)


@step('I compute its factorial')
def compute_its_factorial(step):
    world.number = factorial(world.number)


@step(r'I see the number(\d+)')
def check_number(step expected):
    expected = int(expected)
    assert world.number == expected, f"Got {world.number}"


def factorial(number):
    return -1


li
