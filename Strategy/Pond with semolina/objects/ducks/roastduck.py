from objects.ducks.duck import Duck
from actions.fly.flyingtype import FlyNoWay
from actions.quack.quackingtype import RoastedQuack
from actions.swim.swimtypes import NotSwim


class RoastDuck(Duck):
    _fly_behavior = FlyNoWay()
    _quack_behavior = RoastedQuack()
    _swim_behavior = NotSwim()

    def __repr__(self):
        return "Я жареная утка"
