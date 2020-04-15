from actions.fly.flybehavior import FlyBehavior
from actions.quack.quackbehavior import QuackBehavior
from actions.swim.swimbehavior import SwimBehavior


class Duck:
    _fly_behavior: FlyBehavior
    _quack_behavior: QuackBehavior
    _swim_behavior: SwimBehavior

    def perform_fly(self):
        self._fly_behavior.fly()

    def perform_quack(self):
        self._quack_behavior.quack()

    def perform_swim(self):
        self._swim_behavior.swim()
