import uuid 

class Client:
    def __init__(self, name, email, position, uid=None) -> None:
        self.uid = uid or uuid.uuid4()
        self.name = name
        self.email = email
        self.position = position
    
    def to_dict(self):
        return vars(self)
    
    @staticmethod
    def schema():
        return ["uid", "name", "email", "position"]