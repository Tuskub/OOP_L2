from .quackbehavior import QuackBehavior


class MuteQuack(QuackBehavior):

    def quack(self):
        print('Молчу')
