from abc import ABC, abstractmethod


class Subject(ABC):

    @abstractmethod
    def register_observer(self):
        pass

    @abstractmethod
    def remove_observer(self):
        pass

    @abstractmethod
    def notify_observer(self):
        pass
