#Sumar números ingresados por el usuario hasta que ingrese 0.

suma = 0
numero = int(input("Ingresa un número (0 para terminar): "))
while numero != 0:
    suma += numero
    numero = int(input("Ingresa otro número (0 para terminar): "))
print("La suma total es:", suma)

#Adivinar un número aleatorio entre 1 y 100 (pistas: "mayor" o "menor").

numero_secreto = 5
intento = int(input("Adivina el número entre 1 y 100: "))

while intento != numero_secreto:
    if intento < numero_secreto:
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")
    intento = int(input("Intenta de nuevo: "))

print("¡Felicidades! Adivinaste el número.")

#Validar contraseña (repetir hasta que coincida con una guardada).

contraseña = "patito123"
entrada = input("Ingresa la contraseña: ")

while entrada != contraseña:
    print("Contraseña incorrecta. Intenta de nuevo.")
    entrada = input("Ingresa la contraseña: ")

print("¡Contraseña correcta! Acceso concedido.")

#Simular un cajero automático (menú: retirar, depositar, salir).

opcion = ""
while opcion != "3":
    print(" Bienvenido a Nuestro cajero ")
    print(" Ingrese 1 para retirar dinero")
    print(" Ingrese 2 para depositar dinero")
    print(" Ingrese 3 para salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        monto = float(input("¿Cuánto deseas retirar? "))
        print("Has retirado $",monto )
    elif opcion == "2":
        monto = float(input("¿Cuánto deseas depositar? "))
        saldo += monto
        print(f"Has depositado ${monto}. Saldo actual: ${saldo}")
    elif opcion == "3":
        print("Gracias por usar el cajero. ¡Hasta luego!")
    else:
        print("Opción no válida. Intenta de nuevo.")


# Calcular la raíz cuadrada usando el método babilónico

valor = 20
epsilon = 0.0001
epsilon_al_cuadrado = epsilon ** 2
aprox = valor / 2
nueva_aprox = 0.5 * (aprox + valor / aprox)

while (nueva_aprox - aprox) ** 2 >= epsilon_al_cuadrado:
    aprox = nueva_aprox
    nueva_aprox = 0.5 * (aprox + valor / aprox)

print(f"La raíz cuadrada aproximada de {valor} es {nueva_aprox}")

# Contar la cantidad de cifras de un número entero

entero = 456
temporal = entero
digitos = 0

while temporal > 0:
    temporal //= 10
    digitos += 1

print(f"El número {entero} tiene {digitos} dígitos.")

# Generar la sucesión de Fibonacci hasta un cierto valor

limite_superior = int(input("Introduce el límite: "))
x, y = 0, 1
fibonacci = [x]

while x <= limite_superior:
    x, y = y, x + y
    if x <= limite_superior:
        fibonacci.append(x)

print(f"Sucesión de Fibonacci hasta {limite_superior}:")
print(fibonacci)

# Detectar números primos dentro de un intervalo

rango_inicio = 10
rango_fin = 50
actual = rango_inicio

while actual <= rango_fin:
    if actual > 1:
        divisor = 2
        primo = True
        while divisor * divisor <= actual:
            if actual % divisor == 0:
                primo = False
                break
            divisor += 1
        if primo:
            print(actual)
    actual += 1

# Simular una cuenta regresiva desde un número dado

cuenta = int(input("Introduce un número para iniciar la cuenta regresiva: "))

while cuenta > 0:
    print(f"Tiempo restante: {cuenta} segundos")
    cuenta -= 1

print("¡Cuenta regresiva completada!")

#Leer archivos línea por línea hasta fin de archivo.
f = open("archivo.txt", "r")
linea = f.readline()
while linea != "":
    print(linea, end="")
    linea = f.readline()
f.close()
print("fin del programa")
# Mientras - while
 
contador = 0 
while contador <= 10:
    print("Numero: ", contador)
    contador += 1