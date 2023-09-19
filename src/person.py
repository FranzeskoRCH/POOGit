from abc import ABC  #para clases abstractas
from typing import List

class Persona(ABC):
    
    def __init__(self, nombre: str, cedula: int) -> None:
        self._nombre = nombre
        self._cedula = cedula
    
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self._cedula, {self._nombre}})'

class Autor (Persona):
    def __init__(self, nombre: str, cedula: int) -> None:
        super().__init__(nombre, cedula)
        self.__libros: List["Libro"] = []

class Gerente (Persona):
    def __init__(self, nombre: str, cedula: int) -> None:
        super().__init__(nombre, cedula)
        self.__editorial: "Editorial" = None #Aún no hay editoriales

class Narrador (Persona):
    def __init__(self, nombre: str, cedula: int) -> None:
        super().__init__(nombre, cedula)
        self.__libros: List["Audiolibro"] = []