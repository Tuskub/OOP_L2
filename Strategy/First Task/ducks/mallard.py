from ducks.duck import Duck
from actions.fly.flywithwings import FlyWithWings
from actions.quack.quack import Quack


class MallardDuck(Duck):
    _fly_behavior = FlyWithWings()
    _quack_behavior = Quack()

    def __repr__(self):
        return "Я кряква"

    def display(self):
        print(self)
