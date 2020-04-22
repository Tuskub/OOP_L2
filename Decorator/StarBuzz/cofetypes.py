from beverage import Beverage


class HouseBlend(Beverage):
    _description = 'Домашний кофе'

    def cost(self):
        return 1.2


class DarkRoast(Beverage):
    _description = 'Темный жареный'

    def cost(self):
        return 1.1


class Espresso(Beverage):
    _description = 'Эспрессо'

    def cost(self):
        return 1.0


class Decaf(Beverage):
    _description = 'Без кофеина'

    def cost(self):
        return 1.3
