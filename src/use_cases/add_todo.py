from src.entities.todo import Todo
from src.repositories.todo_repository import TodoRepository

class AddTodoUseCase:
    def __init__(self, repository: TodoRepository):
        self.repository = repository

    def execute(self, description: str):
        todo = Todo(id=None, description=description, done=False)
        self.repository.add(todo)
        return todo