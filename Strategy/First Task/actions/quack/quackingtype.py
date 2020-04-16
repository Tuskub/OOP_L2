from .quackbehavior import QuackBehavior


class Squeak(QuackBehavior):

    def quack(self):
        print('Пищу')


class Quack(QuackBehavior):

    def quack(self):
        print('Крякаю')


class MuteQuack(QuackBehavior):

    def quack(self):
        print('Молчу')


class RoastedQuack(QuackBehavior):

    def quack(self):
        print('Жаренный кряк')
