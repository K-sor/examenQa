from modelos.persona import Persona
from interfaces.trabajador import Trabajador

class Profesor(Persona, Trabajador):
    def __init__(self, nombre: str, edad: int, especialidad: str) -> None:
        super().__init__(nombre, edad)
        self.especialidad = especialidad

    def mostrar_informacion(self) -> None:
        print(f"Profesor: {self.nombre} | Edad: {self.edad} | Especialidad: {self.especialidad}")

    def trabajar(self) -> None:
        print(f"{self.nombre} está enseñando {self.especialidad}.")
