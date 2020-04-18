from StarBuzz.cofetypes import HouseBlend, DarkRoast, Decaf, Espresso
from StarBuzz.condimentttypes import Milk, Soy, Mocha, Whip


test = HouseBlend()
print(test.cost())
test = Milk(test)
print(test.get_description())
test = Milk(test)
test = Milk(test)
print(test.get_description())
print(test.cost())