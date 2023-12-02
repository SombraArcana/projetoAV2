import uuid

class Tarefa:
    def __init__(self, titulo, descricao, data_limite):
        self.id = str(uuid.uuid4())
        self.titulo = titulo
        self.descricao = descricao
        self.data_limite = data_limite
        self.concluida = False
