from repositorios.profesor_repository import ProfesorRepository
from modelos.profesor import Profesor

class ProfesorService:
    """Lógica de negocio para Profesores (usa el repositorio)."""
    def __init__(self) -> None:
        self.repo = ProfesorRepository()

    def registrar(self, nombre: str, edad: int, especialidad: str) -> None:
        self.repo.agregar(Profesor(nombre, edad, especialidad))

    def listar(self):
        return self.repo.listar()

    def buscar(self, nombre: str):
        return self.repo.buscar_por_nombre(nombre)

    def eliminar(self, nombre: str) -> int:
        return self.repo.eliminar_por_nombre(nombre)
