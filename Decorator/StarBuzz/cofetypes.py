from StarBuzz.beverage import Beverage


class HouseBlend(Beverage):
    description = 'Домашний кофе'

    def cost(self):
        return 1.2


class DarkRoast(Beverage):
    description = 'Темный жареный'

    def cost(self):
        return 1.1


class Espresso(Beverage):
    description = 'Эспрессо'

    def cost(self):
        return 1.0


class Decaf(Beverage):
    description = 'Без кофеина'

    def cost(self):
        return 1.3
