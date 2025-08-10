from modelos.persona import Persona
from interfaces.estudiante import Estudiante

class Alumno(Persona, Estudiante):
    def __init__(self, nombre: str, edad: int, carrera: str) -> None:
        super().__init__(nombre, edad)
        self.carrera = carrera

    def mostrar_informacion(self) -> None:
        print(f"Alumno: {self.nombre} | Edad: {self.edad} | Carrera: {self.carrera}")

    def estudiar(self) -> None:
        print(f"{self.nombre} está estudiando para {self.carrera}.")
