from ducks.duck import Duck
from actions.fly.flynoway import FlyNoWay
from actions.quack.squeak import Squeak


class RubberDuck(Duck):
    _fly_behavior = FlyNoWay()
    _quack_behavior = Squeak()

    def __repr__(self):
        return "Я резиновая утка"

    def display(self):
        print(self)
