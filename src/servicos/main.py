
from TasksService import TasksService
from UsersService import UsersService
from AuthService import AuthService

# Criar usuários
usuario1 = UsersService().criar_usuario('João', 'joao@email.com', 'senha123')
usuario2 = UsersService().criar_usuario('Maria', 'maria@email.com', 'senha456')

# Criar tarefas
TasksService().criar_tarefa('Estudar Python', 'Estudar Python por 1 hora.', '2023-12-31')
TasksService().criar_tarefa('Fazer Compras', 'Comprar mantimentos para casa.', '2023-12-30')

# Realizar login
usuario_logado = AuthService().realizar_login('joao@email.com', 'senha123')

# Marcar tarefa como concluída
TasksService().marcar_como_concluida(1)

# Listar tarefas
print(TasksService().listar_tarefas())

# Realizar logout
AuthService().realizar_logout(usuario_logado['id'])
