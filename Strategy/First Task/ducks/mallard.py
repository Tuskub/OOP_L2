from ducks.duck import Duck
from actions.fly.flywithwings import FlyWithWings
from actions.quack.quack import Quack
from actions.swim.likeduck import SwimLikeDuck


class MallardDuck(Duck):
    _fly_behavior = FlyWithWings()
    _quack_behavior = Quack()
    _swim_behavior = SwimLikeDuck()

    def __repr__(self):
        return "Я кряква"

    def display(self):
        print(self)
