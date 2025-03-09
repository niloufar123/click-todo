from src.repositories.todo_repository import TodoRepository

class ListTodosUseCase:
    def __init__(self, repository: TodoRepository):
        self.repository = repository

    def execute(self):
        return self.repository.get_all()