from abc import ABC, abstractmethod


class BaseManager(ABC):

    @abstractmethod
    def create(self, model) -> ...:
        pass

    @abstractmethod
    def read(self, id: int) -> ...:
        pass

    @abstractmethod
    def update(self, id: int, model) -> ...:
        pass

    @abstractmethod
    def delete(self, id: int) -> ...:
        pass


class DBManager(BaseManager):
    pass
