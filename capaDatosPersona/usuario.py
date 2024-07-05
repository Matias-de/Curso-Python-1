class Usuario:
    def __init__(self, idUsuario=None, username=None, password=None):
        self._idUsuario = idUsuario
        self._username = username
        self._password = password

    def __str__(self):
        return f'Usuario: {self._idUsuario}, {self._username}, {self._password}'

    @property
    def idUsuario(self):
        return self._idUsuario

    @idUsuario.setter
    def idUsuario(self, idUsuario):
        self._idUsuario = idUsuario

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password
