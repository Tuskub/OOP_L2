from objects.displayable import Displayable
from actions.quack.quackbehavior import QuackBehavior


class HuntingDecoy(Displayable):
    _quack_behavior: QuackBehavior

    def perform_quack(self):
        self._quack_behavior.quack()

    def display(self):
        print(self)
