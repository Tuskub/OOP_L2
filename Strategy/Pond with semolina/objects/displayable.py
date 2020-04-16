from abc import ABC, abstractmethod


class Displayable(ABC):

    @abstractmethod
    def display(self):
        pass
