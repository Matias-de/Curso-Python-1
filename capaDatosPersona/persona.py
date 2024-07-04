from logger_base import log


class Persona:
    def __init__(self, idPersona=None, nombre=None, apellido=None, email=None): #el none es para omitir darles un valor al crearlos
        self._idPersona = idPersona
        self._nombre = nombre
        self._apellido = apellido
        self._email = email

    def __str__(self):
        return f'''
            ID Persona: {self._idPersona}, Nombre: {self._nombre}
            Apellido: {self._apellido}, Email: {self._email}
        '''

    @property
    def idPersona(self):
        return self._idPersona

    @idPersona.setter
    def idPersona(self, idPersona):
        self._idPersona = idPersona

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email


if __name__ == '__main__':
    persona1 = Persona(1, 'Juan', 'Perez', 'Jperez@gmail.com')
    log.debug(persona1)
    # Simular un insert

    persona1 = Persona(nombre='Juan', apellido='Perez', email='Jperez@gmail.com')
    log.debug(persona1)
    #Simular un delete

    persona1 = Persona(idPersona=1)
    log.debug(persona1)