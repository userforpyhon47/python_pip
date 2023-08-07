import click
from clients.models import Client
from clients.services import Client_Service

@click.group()
def client_manager():
    """Manages clients lifecycle"""
    pass


@client_manager.command()
@click.option("--name", "-n", type=str, prompt=True, help="The client name")
@click.option("--email", "-e", type=str, prompt=True, help="The client email")
@click.option("--position", "-p", type=str, prompt=True, help="The client position")
@click.pass_context
def create_client(ctx, name, email, position):
    """Command to create client"""
    client_service = Client_Service(ctx.obj.get("table_name"))
    client = Client(name, email, position)
    client_service.create_client(client)


@client_manager.command()
@click.pass_context
def list_client(ctx):
    """Command to list clients"""
    client_service = Client_Service(ctx.obj.get("table_name"))
    client_list = client_service.list_clients()
    for item in client_list:
        for v in item.values():
            click.echo(f"{v} | ", nl=False)
        click.echo("")

    return client_list

@client_manager.command()
@click.option("--uid", "-u", type=str, prompt=True, help="The client id")
@click.pass_context
def update_client(ctx, uid):
    """Command to update a client"""
    client_service = Client_Service(ctx.obj.get("table_name"))

    client_tbu = [item for item in client_service.list_clients() if item.get("uid") == uid]

    if client_tbu:
        updated_client = __update_client_flow(Client(**client_tbu[0]))
        if click.confirm("Are you sure you want to commit the changes?"):
            client_service.update_client(uid, updated_client)
    else:
        click.echo(f"Not found! client id '{uid}'")
    

#@click.confirm("Confirm the changes?")
def __update_client_flow(client):
    """Updates client information"""
    client.name = click.prompt(f"New name: ", type=str, default=client.name)
    client.email = click.prompt(f"New email: ", type=str, default=client.email)
    client.position = click.prompt(f"New position: ", type=str, default=client.position)

    return client


@client_manager.command()
@click.option("--uid", "-u", type=str, prompt=True, help="The client id")
@click.pass_context
def delete_client(ctx, uid):
    """Command to delete client"""
    client_service = Client_Service(ctx.obj.get("table_name"))
    client_tbd = [item for item in client_service.list_clients() if item.get("uid") == uid]

    if client_tbd:
        if click.confirm("Are you sure you want to commit the changes?"):
            client_service.delete_client(uid)
    else:
        click.echo(f"Not found! client id '{uid}'")
    
