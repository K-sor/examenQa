from repositorios.alumno_repository import AlumnoRepository
from modelos.alumno import Alumno

class AlumnoService:
    """Lógica de negocio para Alumnos (usa el repositorio)."""
    def __init__(self) -> None:
        self.repo = AlumnoRepository()

    def registrar(self, nombre: str, edad: int, carrera: str) -> None:
        self.repo.agregar(Alumno(nombre, edad, carrera))

    def listar(self):
        return self.repo.listar()

    def buscar(self, nombre: str):
        return self.repo.buscar_por_nombre(nombre)

    def eliminar(self, nombre: str) -> int:
        return self.repo.eliminar_por_nombre(nombre)
