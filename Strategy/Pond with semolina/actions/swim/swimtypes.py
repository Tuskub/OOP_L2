from .swimbehavior import SwimBehavior


class SwimLikeDuck(SwimBehavior):

    def swim(self):
        return 'Плаваю, как утка'


class SwimLikeRubber(SwimBehavior):

    def swim(self):
        return 'Плаваю, как резина'


class SwimLikeWood(SwimBehavior):

    def swim(self):
        return 'Плаваю, как дерево'


class NotSwim(SwimBehavior):

    def swim(self):
        return 'Не плаваю'
