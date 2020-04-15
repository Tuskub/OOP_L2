from actions.fly.flybehavior import FlyBehavior
from actions.quack.quackbehavior import QuackBehavior


class Duck:
    _fly_behavior: FlyBehavior
    _quack_behavior: QuackBehavior

    def perform_fly(self):
        self._fly_behavior.fly()

    def perform_quack(self):
        self._quack_behavior.quack()

