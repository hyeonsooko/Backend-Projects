import click # type: ignore

@click.group()
def main():
    pass

@main.command()
@click.argument('description')
def add(description):
    click.echo(f"{description} is added")

@main.command()
@click.option('--todo', default=None,  required=False, help="list all tasks to do.")
@click.option('--done', default=None, help="list all tasks done.")
def list(todo, done):
    if (todo != None):
        click.echo("todo list")
    elif (done != None):
        click.echo("done list")
    else:
        click.echo("listing")

if __name__ == '__main__':
    main()