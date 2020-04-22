from abc import ABC, abstractmethod
from beverage import Beverage
from collections import Counter


class CondimentDecorator(Beverage, ABC):
    beverage: Beverage

    def get_description(self):
        nums = {1: '', 2: 'Double', 3: 'Triple'}
        collected_disc = Counter(self._collect_description())
        return ', '.join(map(lambda word: f"{nums.get(collected_disc[word],'Many')} {word}".strip(),
                             collected_disc))

    def _collect_description(self):
        return [self._description] + self.beverage._collect_description()
