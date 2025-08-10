from modelos.profesor import Profesor
from modelos.alumno import Alumno

def main() -> None:
    # Instancias de ejemplo
    profesor = Profesor("Luis", 40, "Programación")
    alumno = Alumno("Ana", 20, "Ingeniería en Sistemas")

    # Uso de la clase abstracta a través de las concretas + interfaces
    profesor.mostrar_informacion()
    profesor.trabajar()

    alumno.mostrar_informacion()
    alumno.estudiar()

if __name__ == "__main__":
    main()
