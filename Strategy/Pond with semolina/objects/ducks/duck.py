from objects.displayable import Displayable
from actions.fly.flybehavior import FlyBehavior
from actions.quack.quackbehavior import QuackBehavior
from actions.swim.swimbehavior import SwimBehavior


class Duck(Displayable):
    _fly_behavior: FlyBehavior
    _quack_behavior: QuackBehavior
    _swim_behavior: SwimBehavior

    def perform_fly(self):
        return self._fly_behavior.fly()

    def perform_quack(self):
        return self._quack_behavior.quack()

    def perform_swim(self):
        return self._swim_behavior.swim()

    def display(self):
        print(self)
