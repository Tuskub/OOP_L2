from abc import ABC, abstractmethod


class SwimBehavior(ABC):

    @abstractmethod
    def swim(self):
        pass
