import click
from clients.commands import client_manager

TABLE_NAME = ".clients.csv"

@click.group()
@click.pass_context
def main(ctx):
    ctx.obj = {}
    ctx.obj["table_name"] = TABLE_NAME

main.add_command(client_manager)


if __name__ == "__main__":
    pass



