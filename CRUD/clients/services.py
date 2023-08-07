import os
import csv
from clients.models import Client

class Client_Service:
    def __init__(self, table_name) -> None:
        self.table_name = table_name

    def create_client(self, client):
        with open(self.table_name, mode="a", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=Client.schema())
            writer.writerow(client.to_dict())
    
    def list_clients(self):
        with open(self.table_name, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file, fieldnames=Client.schema())
            return list(reader)
    
    def list_clients(self):
        with open(self.table_name, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file, fieldnames=Client.schema())
            return list(reader)
    
    def update_client(self, uid, client):
        updated_clients = []
        for item in self.list_clients():
            if uid == item.get("uid"):
                updated_clients.append(client.to_dict())
            else:
                updated_clients.append(item)
        
        self.__save_to_disk(updated_clients)
                
    def delete_client(self, uid):
        updated_clients = []
        for item in self.list_clients():
            if uid != item.get("uid"):
                updated_clients.append(item)
        
        self.__save_to_disk(updated_clients)
    
    def __save_to_disk(self, updated_clients):
        with open(f"{self.table_name}.tmp", mode="w", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=Client.schema())
            for item in updated_clients:
                writer.writerow(item)
        try:
            os.remove(self.table_name)
            os.rename(f"{self.table_name}.tmp", self.table_name)
        except Exception as exc:
            print(f"Failed!: {exc}")