from ducks.duck import Duck
from actions.fly.flyingtype import FlyWithWings
from actions.quack.quackingtype import Quack
from actions.swim.swimtypes import SwimLikeDuck


class RedheadDuck(Duck):
    _fly_behavior = FlyWithWings()
    _quack_behavior = Quack()
    _swim_behavior = SwimLikeDuck()

    def __repr__(self):
        return "Я рыжая утка"

    def display(self):
        print(self)
