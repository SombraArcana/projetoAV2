class TasksService:
    tasks = []

    def criar_tarefa(self, titulo, descricao, data_limite):
        nova_tarefa = {
            'titulo': titulo,
            'descricao': descricao,
            'data_limite': data_limite,
            'concluida': False
        }
        self.tasks.append(nova_tarefa)
        return nova_tarefa

    def listar_tarefas(self):
        return self.tasks

    def marcar_como_concluida(self, id_tarefa):
        for tarefa in self.tasks:
            if tarefa['id'] == id_tarefa:
                tarefa['concluida'] = True
                return tarefa

    def editar_tarefa(self, id_tarefa, titulo, descricao, data_limite):
        for tarefa in self.tasks:
            if tarefa['id'] == id_tarefa:
                tarefa['titulo'] = titulo
                tarefa['descricao'] = descricao
                tarefa['data_limite'] = data_limite
                return tarefa
