def menuPrincipal():
    print()
    print()
    print("                          Menu")
    print()
    print()
    print("01. Sistema de parques nacionales.")
    print("02. Control de etiquetados.")
    print("03. Proceso de alimentación.")
    print("04. Contenedores")
    print("05. Salir")
    print()


while True:
    menuPrincipal()
    opc = int(input("Ingrese el ejercicio: "))
    print()
    if opc == 1:
        # inicializar contadores
        niños = 0
        adolescentes = 0
        mayores_edad = 0
        adultos_edad = 0
        # Solicitar datos
        nombre_parque = input("Nombre del parque: ")
        cantidad_usuarios = int(input("Cantidad de usuarios: "))
        # Obtener rango de edades
        for i in range(cantidad_usuarios):
            edad = int(input("edad -> "))
            if edad < 12:
                niños += 1
            elif edad >= 12 and edad < 18:
                adolescentes += 1
            elif edad >= 18 and edad < 65:
                mayores_edad += 1
            elif edad >= 65:
                adultos_edad += 1
        print()
        print(f"""\t.:Paquete:.
Parque Nacional: {nombre_parque}
Niños: {niños}. Monto: ¢0
Adolescentes: {adolescentes}. Monto: ¢{adolescentes*1000}
Mayores de edad: {mayores_edad}. Monto: ¢{mayores_edad*1500}
Adultos mayores: {adultos_edad}. Monto: ¢0
Monto total: ¢{adolescentes*1000+mayores_edad*1500}""")
        print()
    elif opc == 2:
        #inicialización de variables
        buenas_a = 0
        buenas_b = 0
        buenas_c = 0
        buenas_d = 0
        malas_a = 0
        malas_b = 0
        malas_c = 0
        malas_d = 0
        print()
        while True:
            print()
            print("""\t.:Menu:.
01. Ingreso de etiquetado en buen estado
02. Ingreso de etiquetado en mal estado
03. Cantidad procesada
04. Salir
""")        
            #Opciones con un if anidado
            opc = int(input("Ingrese una opción: "))
            if opc == 1:
                cantidad_etiquetado = int(input("Cantidad de etiquetado: "))
                print("Categorías: A, B, C y D")
                for i in range(cantidad_etiquetado):
                    # almacenar las etiquetas correspondientes
                    categoria = input("\tCategoría: ")
                    if categoria.upper() == "A":
                        buenas_a += 1
                    elif categoria.upper() == "B":
                        buenas_b += 1
                    elif categoria.upper() == "C":
                        buenas_c += 1
                    elif categoria.upper() == "D":
                        buenas_d += 1
            elif opc == 2:
                cantidad_etiquetado = int(input("Cantidad de etiquetado: "))
                print("Categorías: A, B, C y D")
                for i in range(cantidad_etiquetado):
                    # almacenar las etiquetas correspondientes
                    categoria = input("\tCategoría: ")
                    if categoria.upper() == "A":
                        malas_a += 1
                    elif categoria.upper() == "B":
                        malas_b += 1
                    elif categoria.upper() == "C":
                        malas_c += 1
                    elif categoria.upper() == "D":
                        malas_d += 1
            elif opc == 3:
                
                print(f"""\tCantidad por categoría
Buen estado: A: {buenas_a}, B: {buenas_b}, C: {buenas_c} y D: {buenas_d}
Dañadas: A: {malas_a}, B: {malas_b}, C: {malas_c} y D: {malas_d}
""")
    elif opc == 3:
        #Solitar datos
        pollos = int(input("Cantidad de pollos: "))
        precio_kilo = int(input("Ingrese el precio por cada kg: "))
        #Operaciones aritméticas
        dispensadores = pollos/6
        corrales = pollos/60
        alimento = 0.5*dispensadores
        inversion = alimento * precio_kilo
        print()
        #Mostrar datos
        print(f"""Total de pollos: {pollos}
Dispensadores: {dispensadores:.2f}
Corrales: {corrales:.2f}
Alimento: {alimento:.2f} kg
Total de inversión diaria: ¢{inversion:.2f}
""")
    elif opc == 4:
        print()
        print("\t.:Puerto:.")
        peso_contenedores = 0
        cantidad_contenedores = 0
        #Solicitud de datos e iteracion de los mismos
        barcos = int(input("Cantidad de barcos: "))
        for b in range(barcos):
            contenedores = int(input("Cantidad de contenedores: "))
            for c in range(contenedores):
                peso = float(input("Peso: "))
                peso_contenedores += peso
            cantidad_contenedores += contenedores
        print()
        #Mostrar datos
        print(f"""Cantidad de barcos: {barcos}
Contenedores: {cantidad_contenedores}
Peso total de los contenedores: {peso_contenedores} kg
""")
    elif opc == 5:
        print("CuChao")
        break