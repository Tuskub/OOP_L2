from .flybehavior import FlyBehavior


class FlyWithWings(FlyBehavior):

    def fly(self):
        print('Лечу')


class FlyNoWay(FlyBehavior):

    def fly(self):
        print('Не лечу')
