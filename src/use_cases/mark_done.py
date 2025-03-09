from src.repositories.todo_repository import TodoRepository

class MarkTodoDoneUseCase:
    def __init__(self, repository: TodoRepository):
        self.repository = repository

    def execute(self, id: int):
        todo = self.repository.get_by_id(id)
        if todo:
            todo.done = True
            self.repository.update(todo)
        else:
            raise ValueError("Todo not found")