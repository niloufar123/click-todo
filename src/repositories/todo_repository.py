from abc import ABC, abstractmethod
from src.entities.todo import Todo

class TodoRepository(ABC):
    @abstractmethod
    def add(self, todo: Todo):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, id: int):
        pass

    @abstractmethod
    def update(self, todo: Todo):
        pass

    @abstractmethod
    def delete(self, id: int):
        pass