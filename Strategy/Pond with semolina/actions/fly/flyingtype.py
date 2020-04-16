from .flybehavior import FlyBehavior


class FlyWithWings(FlyBehavior):

    def fly(self):
        return 'Летаю'


class FlyNoWay(FlyBehavior):

    def fly(self):
        return 'Не летаю'
