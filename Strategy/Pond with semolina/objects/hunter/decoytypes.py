from objects.hunter.huntingdecoy import HuntingDecoy
from actions.quack.quackingtype import Quack, Squeak, RoastedQuack


class NormalDuckDecoy(HuntingDecoy):
    _quack_behavior = Quack()

    def __repr__(self):
        return 'Я манок, для нормальной утки'


class SqueakDuckDecoy(HuntingDecoy):
    _quack_behavior = Squeak()

    def __repr__(self):
        return 'Я манок, для пищащих уток'


class RoastedDuckDecoy(HuntingDecoy):
    _quack_behavior = RoastedQuack()

    def __repr__(self):
        return 'Я манок, для жареных уток'
