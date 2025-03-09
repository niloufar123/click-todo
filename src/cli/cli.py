import click
from src.repositories.json_repository import JsonTodoRepository
from src.use_cases.add_todo import AddTodoUseCase
from src.use_cases.list_todos import ListTodosUseCase
from src.use_cases.mark_done import MarkTodoDoneUseCase
from src.use_cases.delete_todo import DeleteTodoUseCase
from src.presenters.list_presenter import ListTodosPresenter

class TodoContext:
    def __init__(self, file_path):
        self.repository = JsonTodoRepository(file_path)

@click.group()
@click.option('--file', default='todos.json', help='Path to the todos file')
@click.pass_context
def cli(ctx, file):
    ctx.obj = TodoContext(file)

@cli.command()
@click.argument('description')
@click.pass_context
def add(ctx, description):
    use_case = AddTodoUseCase(ctx.obj.repository)
    todo = use_case.execute(description)
    click.echo(f"Added todo with id {todo.id}")

@cli.command()
@click.pass_context
def list(ctx):
    use_case = ListTodosUseCase(ctx.obj.repository)
    todos = use_case.execute()
    presenter = ListTodosPresenter()
    formatted = presenter.present(todos)
    click.echo(formatted)

@cli.command()
@click.argument('id', type=int)
@click.pass_context
def done(ctx, id):
    use_case = MarkTodoDoneUseCase(ctx.obj.repository)
    try:
        use_case.execute(id)
        click.echo(f"Marked todo {id} as done")
    except ValueError as e:
        click.echo(str(e))

@cli.command()
@click.argument('id', type=int)
@click.pass_context
def delete(ctx, id):
    use_case = DeleteTodoUseCase(ctx.obj.repository)
    use_case.execute(id)
    click.echo(f"Deleted todo {id}")

if __name__ == '__main__':
    cli()