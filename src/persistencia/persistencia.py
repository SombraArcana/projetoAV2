import json
import uuid


class TarefasPersistencia:
    def __init__(self, caminho: str) -> None:
        super().__init__()
        self.__caminho = caminho

    def __carregar_json(self) -> json:
        try:
            with open(self.__caminho, encoding='utf-8') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}
        return data

    def __salvar_json(self, dados: json):
        with open(self.__caminho, 'w', encoding='utf-8') as outfile:
            json.dump(dados, outfile, sort_keys=True, indent=2, ensure_ascii=False)

    def carregar_tarefas(self) -> json:
        return self.__carregar_json()

    def carregar_tarefa_id(self, key: str) -> json:
        dados = self.__carregar_json()
        return dados[key] if key in dados else {}

    def adicionar_tarefa(self, titulo: str, descricao: str, data_limite: str):
        dados = self.__carregar_json()

        key = str(uuid.uuid4())
        while key in dados:
            key = str(uuid.uuid4())

        nova_tarefa = {
            'titulo': titulo,
            'descricao': descricao,
            'data_limite': data_limite,
            'concluida': False
        }

        dados[key] = nova_tarefa

        self.__salvar_json(dados)

    def marcar_tarefa_como_concluida(self, key: str) -> bool:
        dados = self.__carregar_json()

        if key not in dados:
            return False

        dados[key]['concluida'] = True

        self.__salvar_json(dados)

        return True

    def remover_tarefa(self, key: str) -> bool:
        dados = self.__carregar_json()

        if key in dados:
            del dados[key]

            self.__salvar_json(dados)

            return True

        return False
