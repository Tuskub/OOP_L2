from .flybehavior import FlyBehavior


class FlyNoWay(FlyBehavior):

    def fly(self):
        print('Не лечу')
