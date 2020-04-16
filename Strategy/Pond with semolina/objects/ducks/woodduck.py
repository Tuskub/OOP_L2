from objects.ducks.duck import Duck
from actions.fly.flyingtype import FlyNoWay
from actions.quack.quackingtype import MuteQuack
from actions.swim.swimtypes import SwimLikeWood


class WoodDuck(Duck):
    _fly_behavior = FlyNoWay()
    _quack_behavior = MuteQuack()
    _swim_behavior = SwimLikeWood()

    def __repr__(self):
        return "Я деревянная утка"
