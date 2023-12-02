class UsersService:
    usuarios = []

    def criar_usuario(self, nome, email, senha):
        novo_usuario = {
            'nome': nome,
            'email': email,
            'senha': senha
        }
        self.usuarios.append(novo_usuario)
        return novo_usuario

    def listar_usuarios(self):
        return self.usuarios

    def buscar_usuario_por_email(self, email):
        for usuario in self.usuarios:
            if usuario['email'] == email:
                return usuario
        return None
