from src.entities.todo import Todo

class ListTodosPresenter:
    def present(self, todos: list[Todo]) -> str:
        if not todos:
            return "No todos found."
        lines = []
        for todo in todos:
            status = "[x]" if todo.done else "[ ]"
            lines.append(f"{todo.id}. {todo.description} {status}")
        return "\n".join(lines)