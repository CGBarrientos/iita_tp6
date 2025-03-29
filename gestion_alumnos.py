""""""""""""""""""""""""""""GESTION DE ALUMNOS"""""""""""""""""""""""""""""""""
datos = {
    "alumnos" = []
}
# Cargar datos mediante archivos


def cargar_datos():
    archivo = open("datos.txt", "r")
    for linea in archivo.readlines():
        datos["alumnos"].append(linea + "\n")
    archivo.close()

# Agregar alumno al listado


def agregar_alumno(nombre, apellido, dni, fecha_nacimiento, tutor):
    alumno = {
        "Nombre": nombre,
        "Apellido": apellido,
        "DNI": dni,
        "Fecha de nacimiento": fecha_nacimiento,
        "Tutor": tutor,
        "Notas": [],
        "Faltas": 0,
        "Amonestaciones": 0
    }
    datos["alumnos"].append(alumno)
    print(f"Alumno {Nombre} {Apellido} agregado")

# Mostrar Alumnos


def mostrar_alumnos():
    for iterador in range(len(datos["alumnos"])):
        print(f"Alumno {iterador+1}:")
        print(f"Nombre: {alumno['Nombre']}")
        print(f"Apellido: {alumno['Apellido']}")
        print(f"DNI: {alumno['DNI']}")
        print(f"Fecha de nacimiento: {alumno['Fecha de nacimiento']}")
        print(f"Tutor: {alumno['Tutor']}")
        print(f"Notas: {alumno['Notas']}")
        print(f"Faltas: {alumno['Faltas']}")
        print(f"Amonestaciones: {alumno['Amonestaciones']}")

# Modificar Datos de Alumno


def modificar_datos(indice, clave, valor):
    if indice < len(datos["Alumnos"]):
        datos["Alumnos"][indice][clave] = valor
    else:
        print("Indice invalido")

# Expulsar alumno


def expulsar_alumno(alumno):
    if alumno < len(datos["Alumnos"]):
        datos["Alumnos"].pop(indice)
    else:
        print("Indice invalido")
