from ducks.duck import Duck
from actions.fly.flywithwings import FlyWithWings
from actions.quack.quack import Quack


class RedheadDuck(Duck):
    _fly_behavior = FlyWithWings()
    _quack_behavior = Quack()

    def __repr__(self):
        return "Я рыжая утка"

    def display(self):
        print(self)
