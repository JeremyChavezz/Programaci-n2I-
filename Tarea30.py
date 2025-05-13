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