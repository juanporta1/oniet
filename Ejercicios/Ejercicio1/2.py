
op = 1

while op != 0:
    print("""
        Menu
        1.Averiguar si son aviones superosónicos
        0.Salir
    """)
    
    op = input("Ingrese una opcion: ")
    while op != 0 and op != 1:
        op = input("Ingrese una opcion valida: ")
    
    if op == "1":
        velocidad = 1
        velocidades = []
        while velocidad != 0:
            velocidad = input("Ingrese la velocidad del avion en km/h (0 para terminar el ingreso): ")
            while not velocidad.isdigit():
                velocidad = input("Vuelva a ingresarla")