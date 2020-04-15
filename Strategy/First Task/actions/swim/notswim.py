from .swimbehavior import SwimBehavior


class NotSwim(SwimBehavior):

    def swim(self):
        print('Не плаваю')
