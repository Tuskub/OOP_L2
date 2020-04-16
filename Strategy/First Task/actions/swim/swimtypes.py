from .swimbehavior import SwimBehavior


class SwimLikeDuck(SwimBehavior):

    def swim(self):
        print('Плаваю, как утка')


class SwimLikeRubber(SwimBehavior):

    def swim(self):
        print('Плаваю, как резина')


class SwimLikeWood(SwimBehavior):

    def swim(self):
        print('Плаваю, как дерево')


class NotSwim(SwimBehavior):

    def swim(self):
        print('Не плаваю')
