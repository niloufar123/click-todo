import click



@click.group
def mycommands():
    pass




@click.command()
@click.option("--name",prompt="Enter your name: ",help="The name of the user")
def hello(name):
    click.echo(f"Hello {name}!")


PRIORITIES={
    "o":"Optional",
    "l":"Low",
    "m":"Medium",
    "h":"High",
    "c":"Crucial"
}

@click.command()
@click.argument("priority",type=click.Choice(PRIORITIES.keys()),default="m")
@click.argument("todofile",type=click.Path(exists=False),required=0)
@click.option("-n","--name",prompt="Enter the todo name ",help="The name of the todo item")
@click.option("-d","--desc",prompt="Describe the to do ",help="The description of the todo item")

def add_todo(name,desc,priority,todofile):
    filename=todofile if todofile is not None else "mytodos.txt"
    with open(filename,"+a") as f:
        f.write(f"{name}: {desc} ---> Priority:{PRIORITIES[priority]}")

@click.command()
@click.argument("idx",type=int,required=1)
def del_todo(idx):
    with open("mytodos.txt","r") as f:
        todoList=f.read().splitlines()
        todoList.pop(idx)
    with open("mytodos.txt","w") as f:
        f.write("\n".join(todoList))
        f.write("\n")

@click.command()
@click.option("-p","--priority",type=click.Choice(PRIORITIES.keys()))
@click.argument("todofile",type=click.Path(exists=True),required=0)

def list_todo(priority,todofile):
    filename=todofile if todofile is not None else "mytodos.txt"
    with open(filename , "r") as f:
        todolist=f.read().splitlines()
        if priority is None:
            for idx,todo in enumerate(todolist):
                print(f"({idx}) - {todo}")

        else :
            for idx,todo in enumerate (todolist):
                if f"[Priority: {PRIORITIES[priority]}]" in todo:
                    print(f"({idx}) - {todo}")

mycommands.add_command(hello)
mycommands.add_command(add_todo)
mycommands.add_command(del_todo)
mycommands.add_command(list_todo)
if __name__=="__main__":
    mycommands()