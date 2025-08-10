from abc import ABC, abstractmethod

class Trabajador(ABC):
    @abstractmethod
    def trabajar(self) -> None:
        """Realiza el trabajo asignado."""
        raise NotImplementedError
