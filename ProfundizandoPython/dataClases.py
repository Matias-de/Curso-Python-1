from dataclasses import dataclass
from typing import ClassVar


@dataclass(eq=True, frozen=True)
class Domicilio:
    calle: str
    numero: int = range(9999)


@dataclass(eq=True, frozen=True)
class Persona:
    nombre: str
    apellido: str
    contadorPersonas: ClassVar[int] = 0
    domicilio: Domicilio

    def __post_init__(self):
        if not self.nombre or not self.apellido:
            raise ValueError(f'Valor "nombre" o apellido vacio')


domicilio1 = Domicilio('Falucho', 2334)
persona1 = Persona('Juan', 'Perez', domicilio1)
print(f'{persona1!r}')  #es lo mismo que llamar el print normal, llama al repr
print(f'Variable clase: {Persona.contadorPersonas}')
print(f'Variables de instancia: {persona1.__dict__}')
#variable con valores vacios
personaVacia = Persona('Carla', 'Gomez', Domicilio('12 de Octubre', 4321))
print(f'Persona vacia: {personaVacia}')
#revisar igualdad entre objetos (__eq__)
persona2 = Persona('Juan', 'Perez', Domicilio('Falucho', 2334))
print(f'Objetos iguales?: {persona1 == persona2}')
#agregar esta clase a una coleccion con frozen = True
#coleccion = {persona1, persona2} #los dataclass son mutables, no deja desde el principio, hay que agregar el parametro frozen)
#print(coleccion)
