
def crearMatriz(t):
    matriz = []
    for n in range(t):
        matriz.append([])
        for m in range(t):
            numero = input(f"Ingrese la posicion {n+1}{m+1}: ")
            while True:
                try: 
                    numero = float(numero)
                    break
                except:
                    numero = input("Ingrese el numero nuevamente(Si el numero es negativo, unicamente ponga un signo): ")
            if numero == int(numero):
                numero = int(numero)
            matriz[n].append(numero)
            print("Asi se ve su matriz actualmente: ")
            for i in matriz:
                print(i)
    return matriz
t = 1   
while t != 0:    
    print("""
        Menu
        ¿De que tamaño quiere que sean las matrices?:
        Para 3x3 ingrese 3.
        Para 4x4 ingrese 4.
        Ingrese 0 para terminar el programa.
    """)
              
    t = 1
    while t != 3 and t != 4 and t != 0:
        t = input("Tamaño de la matriz: ")
        if t.isdigit() and (t == "3" or t == "4" or t == "0"):
            t = int(t)
            break
        else:
            print("Ingreso un dato no válido, vuelva a intentarlo.")
    if t != 0:
        print("")
        print("Armado de la primer matriz: ")
        print("")
        matriz1 = crearMatriz(t)

        print("")
        print("Armado de la segunda matriz: ")
        print("")
        matriz2 = crearMatriz(t)

        print("")
        print("Sumando las matrices")
        print("")

        suma = []
        for n in range(t):
            suma.append([])
            for m in range(t):
                s = matriz1[n][m] + matriz2[n][m]
                if s == int(s):
                    s = int(s)
                else:
                    round(s,2)
                suma[n].append(s)

        for i in range(t):
            
            if i == 1:
                print(matriz1[i],"+",matriz2[i],"=", suma[i])
            else:
                print(matriz1[i]," ", matriz2[i], " ", suma[i])
        print("")
        print("Otra forma de visualizar la matriz: ")
        print("")

        for n in range(t):
            for m in range(t):
                print(f"Posicion {n+1}{m+1}: ", suma[n][m])
print("Gracias por utilizar el programa.")