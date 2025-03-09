import json
from pathlib import Path
from src.entities.todo import Todo
from src.repositories.todo_repository import TodoRepository

class JsonTodoRepository(TodoRepository):
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
        if not self.file_path.exists():
            self.file_path.write_text('[]')

    def _load_todos(self):
        with self.file_path.open('r') as f:
            data = json.load(f)
        return [Todo(**item) for item in data]

    def _save_todos(self, todos):
        data = [todo.__dict__ for todo in todos]
        with self.file_path.open('w') as f:
            json.dump(data, f, indent=2)

    def add(self, todo):
        if todo.id is not None:
            raise ValueError("Cannot add todo with existing id")
        todos = self._load_todos()
        max_id = max([t.id for t in todos], default=0)
        todo.id = max_id + 1
        todos.append(todo)
        self._save_todos(todos)

    def get_all(self):
        return self._load_todos()

    def get_by_id(self, id):
        todos = self._load_todos()
        for todo in todos:
            if todo.id == id:
                return todo
        return None

    def update(self, updated_todo):
        if updated_todo.id is None:
            raise ValueError("Cannot update todo without id")
        todos = self._load_todos()
        for i, todo in enumerate(todos):
            if todo.id == updated_todo.id:
                todos[i] = updated_todo
                self._save_todos(todos)
                return
        raise ValueError("Todo not found")

    def delete(self, id):
        todos = self._load_todos()
        todos = [todo for todo in todos if todo.id != id]
        self._save_todos(todos)