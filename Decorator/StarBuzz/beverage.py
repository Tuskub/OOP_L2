from abc import ABC, abstractmethod


class Beverage(ABC):
    _description = 'Неизвестный напиток'

    def _collect_description(self):
        return [self._description]

    def get_description(self):
        return self._description

    @abstractmethod
    def cost(self):
        pass
