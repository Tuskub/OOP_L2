from beverage import Beverage
from condiment import CondimentDecorator


class Milk(CondimentDecorator):
    _description = 'Milk'
    milk_cost = .3

    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def cost(self):
        return self.milk_cost + self.beverage.cost()


class Mocha(CondimentDecorator):
    _description = 'Mocha'
    mocha_cost = .23

    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def cost(self):
        return self.mocha_cost + self.beverage.cost()


class Soy(CondimentDecorator):
    _description = 'Soy'
    soy_cost = .23

    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def cost(self):
        return self.soy_cost + self.beverage.cost()


class Whip(CondimentDecorator):
    _description = 'Whip'
    whip_cost = .13

    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def cost(self):
        return self.whip_cost + self.beverage.cost()
