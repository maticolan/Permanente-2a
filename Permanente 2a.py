a = True
libros_disponibles_estudiantes=[]
libros_prestados_estudiantes=[]
libros_disponibles_docentes=[]
libros_prestados_docentes=[]

libros_estudiantes={
    'El Caballero Carmelo':'Abraham Valdelomar',
    'El Quijote':'Miguel de Cervantes',
    'La Odisea':'Homero',
    'La Divina Comedia':'Dante Alighieri',
    'Hamlet':'William Shakespeare',
    'Las Mil y Una Noches':'Anónimo',
    'Cien Años de Soledad':'Gabriel García Márquez'
    }

libros1=libros_estudiantes.copy()
del libros1['Hamlet']
del libros1['Cien Años de Soledad']
for key, value in libros1.items():
    libros_disponibles_estudiantes.append(key)

libros2=libros_estudiantes.copy()
del libros2['El Caballero Carmelo']
del libros2['El Quijote']
del libros2['La Odisea']
del libros2['La Divina Comedia']
del libros2['Las Mil y Una Noches']
for key, value in libros2.items():
    libros_prestados_estudiantes.append(key)

libros_docentes={
    'El Caballero Carmelo':'Abraham Valdelomar',
    'El Quijote':'Miguel de Cervantes',
    'La Odisea':'Homero',
    'La Divina Comedia':'Dante Alighieri',
    'Hamlet':'William Shakespeare',
    'Las Mil y Una Noches':'Anónimo',
    'Cien Años de Soledad':'Gabriel García Márquez',
    'Curso de lingüistica general':'Ferdinand De Saussure',
    'El proceso de la comunicación: teoría y práctica':'David Berlo',
    'Fundamentos y fines de la educación':'Francisco Ruiz',
    'Metodología del trabajo intelectual':'Jorge Bernedo',
    'Introduction To Computation And Programming Using Python':'John Guttag'
    }

libros3=libros_docentes.copy()
del libros3['Hamlet']
del libros3['Cien Años de Soledad']
del libros3['Introduction To Computation And Programming Using Python']
for key, value in libros3.items():
    libros_disponibles_docentes.append(key)

libros4=libros_docentes.copy()
del libros4['El Caballero Carmelo']
del libros4['El Quijote']
del libros4['La Odisea']
del libros4['La Divina Comedia']
del libros4['Las Mil y Una Noches']
del libros4['Metodología del trabajo intelectual']
del libros4['Curso de lingüistica general']
del libros4['El proceso de la comunicación: teoría y práctica']
del libros4['Fundamentos y fines de la educación']
for key, value in libros4.items():
    libros_prestados_docentes.append(key)

def prestar_estudiante():
    print(libros_disponibles_estudiantes)
    print()
    print("¿Qué libro desea prestarse?")
    oplp = int(input("Ingrese la posición del libro: "))
    if oplp == 1:
        libros_disponibles_estudiantes.remove('El Caballero Carmelo')
        libros_disponibles_docentes.remove('El Caballero Carmelo')
        libros_prestados_estudiantes.insert(0,'El Caballero Carmelo')
        libros_prestados_docentes.insert(0,'El Caballero Carmelo')
    elif oplp == 2:
        libros_disponibles_estudiantes.remove('El Quijote')
        libros_disponibles_docentes.remove('El Quijote')
        libros_prestados_estudiantes.insert(0,'El Quijote')
        libros_prestados_docentes.insert(0,'El Quijote')
    elif oplp == 3:
        libros_disponibles_estudiantes.remove('La Odisea')
        libros_disponibles_docentes.remove('La Odisea')
        libros_prestados_estudiantes.insert(0,'La Odisea')
        libros_prestados_docentes.insert(0,'La Odisea')
    elif oplp == 4:
        libros_disponibles_estudiantes.remove('La Divina Comedia')
        libros_disponibles_docentes.remove('La Divina Comedia')
        libros_prestados_estudiantes.insert(0,'La Divina Comedia')
        libros_prestados_docentes.insert(0,'La Divina Comedia')
    elif oplp == 5:
        libros_disponibles_estudiantes.remove('Las Mil y Una Noches')
        libros_disponibles_docentes.remove('Las Mil y Una Noches')
        libros_prestados_estudiantes.insert(0,'Las Mil y Una Noches')
        libros_prestados_docentes.insert(0,'Las Mil y Una Noches')
    else:
        print("No existe la opción seleccionada.")
        print("Inténtelo de nuevo.")        
        prestar_estudiante()

def prestar_docente():
    print(libros_disponibles_docentes)
    print()
    print("¿Qué libro desea prestarse?")
    oplp = int(input("Ingrese la posición del libro: "))
    if oplp == 1:
        libros_disponibles_docentes.remove('El Caballero Carmelo')
        libros_disponibles_estudiantes.remove('El Caballero Carmelo')
        libros_prestados_docentes.insert(0,'El Caballero Carmelo')
        libros_prestados_estudiantes.insert(0,'El Caballero Carmelo')
    elif oplp == 2:
        libros_disponibles_docentes.remove('El Quijote')
        libros_disponibles_estudiantes.remove('El Quijote')
        libros_prestados_docentes.insert(0,'El Quijote')
        libros_prestados_estudiantes.insert(0,'El Quijote')
    elif oplp == 3:
        libros_disponibles_docentes.remove('La Odisea')
        libros_disponibles_estudiantes.remove('La Odisea')
        libros_prestados_docentes.insert(0,'La Odisea')
        libros_prestados_estudiantes.insert(0,'La Odisea')
    elif oplp == 4:
        libros_disponibles_docentes.remove('La Divina Comedia')
        libros_disponibles_estudiantes.remove('La Divina Comedia')
        libros_prestados_docentes.insert(0,'La Divina Comedia')
        libros_prestados_estudiantes.insert(0,'La Divina Comedia')
    elif oplp == 5:
        libros_disponibles_docentes.remove('Las Mil y Una Noches')
        libros_disponibles_estudiantes.remove('Las Mil y Una Noches')
        libros_prestados_docentes.insert(0,'Las Mil y Una Noches')
        libros_prestados_estudiantes.insert(0,'Las Mil y Una Noches')
    elif oplp == 6:
        libros_disponibles_docentes.remove('Curso de lingüistica general')
        libros_prestados_docentes.insert(0,'Curso de lingüistica general')
    elif oplp == 7:
        libros_disponibles_docentes.remove('El proceso de la comunicación: teoría y práctica')
        libros_prestados_docentes.insert(0,'El proceso de la comunicación: teoría y práctica')
    elif oplp == 8:
        libros_disponibles_docentes.remove('Fundamentos y fines de la educación')
        libros_prestados_docentes.insert(0,'Fundamentos y fines de la educación')
    elif oplp == 9:
        libros_disponibles_docentes.remove('Metodología del trabajo intelectual')
        libros_prestados_docentes.insert(0,'Metodología del trabajo intelectual')
    else:
        print("No existe la opción seleccionada.")
        print("Inténtelo de nuevo.")  
        prestar_docente()

def menu_principal():
    print()
    print("\t.:MENU PRINCIPAL:")
    print("1.Estudiante")
    print("2.Docente")
    print("3.Salir")
    opmp=str(input("Elige el rol: "))
    if opmp=="1":
        menu_estudiante()
        menu_principal()
    if opmp=="2":
        contra = input("Ingrese la contraseña: ")
        while contra != "2022":
            contra = input("Contraseña incorrecta, inténtelo de nuevo: ")
        else:
            menu_docente()  
        menu_principal()
    if opmp=="3":
        Salir()
    else:
        print("No existe el rol ingresado.")
        print("Inténtelo de nuevo.")
        menu_principal()
        
def menu_estudiante():
    print()
    print("\t.:BIENVENIDO ESTUDIANTE:")
    print("1. Ver la lista de los libros")
    print("2. Ver los autores de los libros")
    print("3. Ver la lista de los libros prestados")
    print("4. Ver la lista de los libros disponibles")
    print("5. Prestarse un libro")
    print("6. Salir")
    print()
    opme = str(input("Elige una opción: "))
    print()
    if opme == "1":
        for keys, values in libros_estudiantes.items():
            print(keys)
        menu_estudiante()
    elif opme == "2":
        for keys, values in libros_estudiantes.items():
            print(values)
        menu_estudiante()
    elif opme == "3":
        print(libros_prestados_estudiantes)
        menu_estudiante()    
    elif opme == "4":
        print(libros_disponibles_estudiantes)
        menu_estudiante()
    elif opme == "5":
        prestar_estudiante()
        menu_estudiante()
    elif opme == "6":
        menu_principal()
    else:
        print("No existe la opción seleccionada.")
        print("Inténtelo de nuevo.")
        menu_estudiante()
        
def menu_docente():
    print()
    print("\t.:BIENVENIDO DOCENTE:")
    print("1. Ver la lista de los libros")
    print("2. Ver los autores de los libros")
    print("3. Ver la lista de los libros prestados")
    print("4. Ver la lista de los libros disponibles")
    print("5. Prestarse un libro")
    print("6. Salir")
    print()
    opmd = str(input("Elige una opción: "))
    print()
    if opmd == "1":
        for keys, values in libros_docentes.items():
            print(keys)
        menu_docente()
    elif opmd == "2":
        for keys, values in libros_docentes.items():
            print(values)
        menu_docente()
    elif opmd == "3":
        print(libros_prestados_docentes)
        menu_docente()    
    elif opmd == "4":
        print(libros_disponibles_docentes)
        menu_docente()
    elif opmd == "5":
        prestar_docente()
        menu_docente()
    elif opmd == "6":
        menu_principal()
    else:
        print("No existe la opción seleccionada.")
        print("Inténtelo de nuevo.")
        menu_docente()

def Salir():
    while a:
        print("Gracias por utilizar el programa.")
        break

    
print("\t.:BIENVENIDO/A AL SISTEMA:")
print(menu_principal())