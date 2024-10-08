Alumnos = [
    {'nombre': 'Lucio', 'apellido': 'Aguilar', 'edad': 19, 'especialidad': 'Informatica'},
    {'nombre': 'Federico', 'apellido': 'Caracciolo', 'edad': 19, 'especialidad': 'Informatica'},
    {'nombre': 'Luca', 'apellido': 'Pons', 'edad': 18, 'especialidad': 'Construcciones'},
    {'nombre': 'Marcos', 'apellido': 'Funes', 'edad': 19, 'especialidad': 'Informatica'},
    {'nombre': 'Lautaro', 'apellido': 'Montes', 'edad': 19, 'especialidad': 'Informatica'},
    {'nombre': 'Martin', 'apellido': 'Gonzalez', 'edad': 38, 'especialidad': 'Informatica'},
    {'nombre': 'Gonzalo', 'apellido': 'Beckhman', 'edad': 19, 'especialidad': 'Informatica'},
    {'nombre': 'Carlos', 'apellido': 'Colosimo', 'edad': 19, 'especialidad': 'Informatica'},
    {'nombre': 'Giuliano', 'apellido': 'De Giusto', 'edad': 22, 'especialidad': 'Informatica'},
    {'nombre': 'Gaspar', 'apellido': 'Barea', 'edad': 19, 'especialidad': 'Informatica'}
]

def mostrar_alumnos():
    print("Lista de Alumnos:")
    for Alumno in Alumnos:
        print(f"Nombre: {Alumno['nombre']}, Apellido: {Alumno['apellido']}, Edad: {Alumno['edad']}, Especialidad: {Alumno['especialidad']}")

def agregar_alumno(nombre, apellido, edad, especialidad):
    nuevo_alumno = {'nombre': nombre, 'apellido': apellido, 'edad': edad, 'especialidad': especialidad}
    Alumnos.append(nuevo_alumno)

def actualizar_alumno(nombre, apellido, nuevos_datos):
    for alumno in Alumnos:
        if alumno['nombre'] == nombre and alumno['apellido'] == apellido:
            for clave, valor in nuevos_datos.items():
                if clave in alumno:
                    alumno[clave] = valor
            return alumno
    return None

def eliminar_alumno(nombre, apellido):
    global Alumnos
    global alumnos_eliminados  
    alumnos_eliminados = []  
    for alumno in Alumnos:
        if alumno['nombre'] == nombre and alumno['apellido'] == apellido:
            alumnos_eliminados.append(alumno)  
    Alumnos = [alumno for alumno in Alumnos if not (alumno['nombre'] == nombre and alumno['apellido'] == apellido)]

# Menú principal
while True:
    print("\nOpciones:")
    print("1. Mostrar Alumnos")
    print("2. Agregar Alumno")
    print("3. Actualizar Alumno")
    print("4. Eliminar Alumno")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        mostrar_alumnos()
        
    elif opcion == '2':
        nombre = input("Ingrese el nombre del alumno: ")
        apellido = input("Ingrese el apellido del alumno: ")
        edad = int(input("Ingrese la edad del alumno: "))
        especialidad = input("Ingrese la especialidad del alumno: ")
        agregar_alumno(nombre, apellido, edad, especialidad)
        print("Alumno agregado exitosamente.")
        
    elif opcion == '3':
        nombre = input("Ingrese el nombre del alumno a actualizar: ")
        apellido = input("Ingrese el apellido del alumno a actualizar: ")
        nuevos_datos = {}
        nuevos_datos['edad'] = int(input("Ingrese la nueva edad: "))
        nuevos_datos['especialidad'] = input("Ingrese la nueva especialidad: ")
        alumno_actualizado = actualizar_alumno(nombre, apellido, nuevos_datos)
        if alumno_actualizado:
            print("Alumno actualizado exitosamente.")
        else:
            print("Alumno no encontrado.")
        
    elif opcion == '4':
        nombre = input("Ingrese el nombre del alumno a eliminar: ")
        apellido = input("Ingrese el apellido del alumno a eliminar: ")
        eliminar_alumno(nombre, apellido)
        if alumnos_eliminados:
            print("Alumno eliminado exitosamente.")
        else:
            print("Alumno no encontrado.")
        
    elif opcion == '5':
        print("Saliendo del programa.")
        break
        
    else:
        print("Opción no válida. Intente de nuevo.")