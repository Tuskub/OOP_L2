from abc import ABC, abstractmethod


class Subject(ABC):

    @abstractmethod
    def register_observer(self, subscriber):
        pass

    @abstractmethod
    def remove_observer(self, subscriber):
        pass

    @abstractmethod
    def notify_observer(self):
        pass
