from ducks.duck import Duck
from actions.fly.flyingtype import FlyNoWay
from actions.quack.quackingtype import Squeak
from actions.swim.swimtypes import SwimLikeRubber


class RubberDuck(Duck):
    _fly_behavior = FlyNoWay()
    _quack_behavior = Squeak()
    _swim_behavior = SwimLikeRubber()

    def __repr__(self):
        return "Я резиновая утка"

    def display(self):
        print(self)
