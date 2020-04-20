from abc import ABC, abstractmethod
from beverage import Beverage
from collections import Counter


class CondimentDecorator(Beverage, ABC):
    beverage: Beverage

    def get_description(self):
        nums = {1: '', 2: 'Double', 3: 'Triple'}
        collected_disc = Counter(self.collect_description())
        return ', '.join(map(lambda word: f"{nums.get(collected_disc[word],'Many')} {word}".strip(),
                             collected_disc))

    def collect_description(self):
        return [self.description] + self.beverage.collect_description()
