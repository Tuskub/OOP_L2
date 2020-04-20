from abc import ABC, abstractmethod


class Beverage(ABC):
    description = 'Неизвестный напиток'

    def collect_description(self):
        return [self.description]

    def get_description(self):
        return self.description

    @abstractmethod
    def cost(self):
        pass
