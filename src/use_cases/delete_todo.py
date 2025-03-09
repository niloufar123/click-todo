from src.repositories.todo_repository import TodoRepository

class DeleteTodoUseCase:
    def __init__(self, repository: TodoRepository):
        self.repository = repository

    def execute(self, id: int):
        self.repository.delete(id)