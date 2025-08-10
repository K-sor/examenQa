from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre: str, edad: int) -> None:
        self.nombre = nombre
        self.edad = edad

    @abstractmethod
    def mostrar_informacion(self) -> None:
        """Muestra la información básica de la persona."""
        raise NotImplementedError
