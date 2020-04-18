from abc import ABC, abstractmethod
from StarBuzz.beverage import Beverage


class CondimentDecorator(Beverage, ABC):

    @abstractmethod
    def get_description(self):
        pass
