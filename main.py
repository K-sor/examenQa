from servicios.profesor_service import ProfesorService
from servicios.alumno_service import AlumnoService

def main() -> None:
    prof_srv = ProfesorService()
    alu_srv = AlumnoService()

    # Registrar datos de ejemplo
    prof_srv.registrar("Luis", 40, "Programación")
    prof_srv.registrar("María", 38, "Bases de Datos")

    alu_srv.registrar("Ana", 20, "Ingeniería en Sistemas")
    alu_srv.registrar("Luis", 19, "Ciencias de la Computación")

    print("\n📋 Profesores:")
    for p in prof_srv.listar():
        p.mostrar_informacion()

    print("\n📋 Alumnos:")
    for a in alu_srv.listar():
        a.mostrar_informacion()

    print("\n🔍 Buscar por nombre 'Luis':")
    for p in prof_srv.buscar("Luis"):
        p.mostrar_informacion()
    for a in alu_srv.buscar("Luis"):
        a.mostrar_informacion()

    print("\n🗑️ Eliminar alumno 'Ana':")
    eliminados = alu_srv.eliminar("Ana")
    print(f"Eliminados: {eliminados}")

    print("\n📋 Alumnos (después de eliminar):")
    for a in alu_srv.listar():
        a.mostrar_informacion()

if __name__ == "__main__":
    main()
