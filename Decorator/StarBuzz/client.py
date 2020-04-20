from cofetypes import HouseBlend, DarkRoast, Decaf, Espresso
from condimentttypes import Milk, Soy, Mocha, Whip


test = HouseBlend()
print(test.cost())
test = Milk(test)
test = Soy(test)
test = Whip(test)
test = Whip(test)
test = Mocha(test)
print(test.get_description())
print(test.cost())
