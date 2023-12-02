from users_service import UsersService

class AuthService:
    usuarios_logados = []

    def realizar_login(self, email, senha):
        usuario = UsersService().buscar_usuario_por_email(email)
        if usuario and usuario['senha'] == senha:
            self.usuarios_logados.append(usuario)
            return usuario
        return None

    def realizar_logout(self, id_usuario):
        for usuario in self.usuarios_logados:
            if usuario['id'] == id_usuario:
                self.usuarios_logados.remove(usuario)
                return True
        return False
