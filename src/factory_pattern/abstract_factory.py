import abc
from shape_game import Circle, Square


class AbstractFactory():
    __metaclass__ = abc.ABCMeta

    @abc.abstractclassmethod()
    def make_object(self):
        return


class CircleFactory(AbstractFactory):
    def make_object(self):
        return Circle()


class SquareFactory(AbstractFactory):
    def make_object(self):
        return Square()


def draw_function(factory):
    drawable = factory.make_object()
    drawable.draw()


def prepare_client():
    squareFactory = SquareFactory()
    draw_function(squareFactory)
    circleFactory = CircleFactory()
    draw_function(circleFactory)
