import uuid

class Usuario:
    def __init__(self, nome, email, senha):
        self.id = str(uuid.uuid4())
        self.nome = nome
        self.email = email
        self.senha = senha
