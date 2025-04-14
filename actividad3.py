def maximo_de_tres(a, b, c):
    return max(a, b, c)

def maximo_de_diez(lista):
    maximo = lista[0]
    for i in range(0, len(lista), 3):
        maximo = max(maximo, maximo_de_tres(lista[i], lista[i+1], lista[i+2]))
    return maximo


def cargar_vector(n):
    vector = []
    for i in range(n):
        valor = int(input(f"Ingrese el valor {i+1}: "))
        vector.append(valor)
    return vector

def suma_vector(vector):
    total = 0
    for num in vector:
        total += num
    print("Suma del vector:", total)
    return total

def suma_vectores(a, b):
    return [a[i] + b[i] for i in range(len(a))]


def contar_vocales(palabra):
    vocales = "aeiouAEIOU"
    contador = 0
    for letra in palabra:
        if letra in vocales:
            contador += 1
    return contador

def contar_consonantes(palabra):
    consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    contador = 0
    for letra in palabra:
        if letra in consonantes:
            contador += 1
    return contador


def min_menu():
    print("Ingrese el numero 1 si quiere sacar una potencia de un numero")
    print("Ingrese el numero 2 si quiere contar la cantidad de digitos de un numero")
    print("Ingrese el numero 3 si quiere saber si un numero es capicua")
    print("Ingrese cualquier otro caracter para salir")

def Pedir_potencia():
    k = int(input("Ingrese el valor de la potencia: "))
    return k

def calcular_potencia(numero, k):
    numero_potenciado = numero ** k
    print(f"El resultado de {numero} elevado a la potencia {k} es: {numero_potenciado}")

def contar_digitos(numero):
    print(f"El numero {numero} tiene {len(str(numero))} digitos")

def es_capicua(numero):
    numero = str(numero)
    if numero == numero[::-1]:
        print(f"El número {numero} es capicúa.")
    else:
        print(f"El número {numero} no es capicúa.")


def cargar_matriz(m, n):
    matriz = []
    for i in range(m):
        fila = []
        for j in range(n):
            valor = int(input(f"Ingrese A[{i}][{j}]: "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

def suma_matrices(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def producto_matrices(a, b):
    return [[a[i][j] * b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def mostrar_matriz(m):
    for fila in m:
        print(fila)

def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Máximo entre 3 números")
        print("2. Máximo entre 10 números")
        print("3. Operaciones con vectores A y B")
        print("4. Contar vocales y consonantes en texto")
        print("5. Menú de funciones matemáticas")
        print("6. Suma o producto de matrices")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            a = int(input("Ingrese número 1: "))
            b = int(input("Ingrese número 2: "))
            c = int(input("Ingrese número 3: "))
            print("Máximo:", maximo_de_tres(a, b, c))

        elif opcion == "2":
            lista = []
            print("Ingrese 10 números:")
            for i in range(10):
                lista.append(int(input(f"Número {i+1}: ")))
            print("Máximo de los 10 números:", maximo_de_diez(lista))

        elif opcion == "3":
            N = int(input("Cantidad de elementos para vector A: "))
            M = int(input("Cantidad de elementos para vector B: "))
            print("Cargando vector A:")
            A = cargar_vector(N)
            print("Cargando vector B:")
            B = cargar_vector(M)
            suma_vector(A)
            suma_vector(B)
            if N == M:
                print("Suma de vectores A+B:", suma_vectores(A, B))
            else:
                print("No se pueden sumar vectores de distinta longitud.")

        elif opcion == "4":
            texto = input("Ingrese una o más oraciones: ")
            palabras = texto.split()
            total_vocales = 0
            total_consonantes = 0
            for palabra in palabras:
                total_vocales += contar_vocales(palabra)
                total_consonantes += contar_consonantes(palabra)
            print("Total de vocales:", total_vocales)
            print("Total de consonantes:", total_consonantes)

        elif opcion == "5":
            min_menu()
            sub = input("Seleccione una opción: ")
            if sub == "1":
                numero = int(input("Ingrese el número base: "))
                k = Pedir_potencia()
                calcular_potencia(numero, k)
            elif sub == "2":
                numero = int(input("Ingrese el número: "))
                contar_digitos(numero)
            elif sub == "3":
                numero = input("Ingrese el número: ")
                es_capicua(numero)
            else:
                print("Saliendo del submenú de funciones matemáticas...")

        elif opcion == "6":
            M = int(input("Cantidad de filas: "))
            N = int(input("Cantidad de columnas: "))
            print("Cargando matriz A:")
            A = cargar_matriz(M, N)
            print("Cargando matriz B:")
            B = cargar_matriz(M, N)
            op = input("¿Suma (s) o Producto (p)?: ").lower()
            if op == 's':
                C = suma_matrices(A, B)
            elif op == 'p':
                C = producto_matrices(A, B)
            else:
                print("Operación inválida.")
                continue
            print("Resultado:")
            mostrar_matriz(C)

        elif opcion == "0":
            print("¡Programa finalizado!")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()


