from .quackbehavior import QuackBehavior


class Squeak(QuackBehavior):

    def quack(self):
        return 'Пищу'


class Quack(QuackBehavior):

    def quack(self):
        return 'Крякаю'


class MuteQuack(QuackBehavior):

    def quack(self):
        return 'Молчу'


class RoastedQuack(QuackBehavior):

    def quack(self):
        return 'Жареный кряк'
