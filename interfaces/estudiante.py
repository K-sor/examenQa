from abc import ABC, abstractmethod

class Estudiante(ABC):
    @abstractmethod
    def estudiar(self) -> None:
        """Realiza actividades de estudio."""
        raise NotImplementedError
