from StarBuzz.beverage import Beverage
from StarBuzz.condiment import CondimentDecorator


class Milk(CondimentDecorator):
    description = 'Молоко'
    beverage: Beverage
    milk_cost = .3

    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def get_description(self):
        return self.description + self.beverage.get_description()

    def cost(self):
        return self.milk_cost + self.beverage.cost()


class Mocha(CondimentDecorator):
    description = 'Шоколад'
    beverage: Beverage
    mocha_cost = .23

    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def get_description(self):
        return self.description + self.beverage.get_description()

    def cost(self):
        return self.mocha_cost + self.beverage.cost()


class Soy(CondimentDecorator):
    description = 'Соя'
    beverage: Beverage
    soy_cost = .23

    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def get_description(self):
        return self.description + self.beverage.get_description()

    def cost(self):
        return self.soy_cost + self.beverage.cost()


class Whip(CondimentDecorator):
    description = 'Взбитые сливки'
    beverage: Beverage
    whip_cost = .13

    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def get_description(self):
        return self.description + self.beverage.get_description()

    def cost(self):
        return self.whip_cost + self.beverage.cost()
