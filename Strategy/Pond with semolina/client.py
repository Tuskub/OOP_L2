from objects.ducks.decoyduck import DecoyDuck
from objects.ducks.mallardduck import MallardDuck
from objects.ducks.redheadduck import RedheadDuck
from objects.ducks.roastduck import RoastDuck
from objects.ducks.rubberduck import RubberDuck
from objects.ducks.woodduck import WoodDuck
from objects.hunter.decoytypes import NormalDuckDecoy, SqueakDuckDecoy, RoastedDuckDecoy


# Ducks
ducks = [DecoyDuck, MallardDuck, RedheadDuck, RoastDuck, RubberDuck, WoodDuck]
for cls in ducks:
    duck = cls()
    print(cls.__name__)
    print(f'-{duck}')
    print(f'-{duck.perform_quack()}')
    print(f'-{duck.perform_fly()}')
    print(f'-{duck.perform_swim()}')
# Hunter's decoys
decoys = [NormalDuckDecoy, SqueakDuckDecoy, RoastedDuckDecoy]
for cls in decoys:
    decoy = cls()
    print(cls.__name__)
    print(f'-{decoy}')
    print(f'-{decoy.perform_quack()}')
