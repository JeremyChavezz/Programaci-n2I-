# Conteo regresivo con while
cuenta = 10

while cuenta >= 1:
    print(cuenta)
    cuenta -= 1

print("¡Despegue!")

# Adivina la palabra secreta
clave_secreta = "Futbol"

while True:
    respuesta = input("Adivina la palabra secreta: ")
    
    if respuesta == clave_secreta:
        print("¡Has adivinado la palabra!")
        break
    else:
        print("Inténtalo de nuevo.")

# Procesador de entradas con continue
while True:
    texto = input("Ingresa un texto: ")
    
    if texto == "#":
        continue
    elif texto == "listo":
        print("¡Procesamiento terminado!")
        break
    else:
        print(texto.upper())
    
# Lista de invitados con for
asistentes = ['Ana', 'Luis', 'Carla', 'Pedro']

for persona in asistentes:
    persona = input("Ingresa el nombre del invitado: ")
    print("Hola " + persona + ", ¡bienvenida a la fiesta!")

# Encontrando el número mayor (for)
valores = [3, 41, 12, 9, 74, 15, 1, 55]
maximo_actual = -1

for valor in valores:
    if valor > maximo_actual:
        maximo_actual = valor

print("El número más grande es:", maximo_actual)

# Conteo de elementos pares (for y condicional)
valores_pares = [2, 5, 8, 11, 14, 17, 20, 23]
contador_pares = 0

for valor in valores_pares:
    if valor % 2 == 0:
        contador_pares += 1

print("Cantidad de números pares:", contador_pares)

# Suma todos los números (FOR)
numeros_lista = [10, 20, 30, 40, 50]
total_suma = 0

for num in numeros_lista:
    total_suma += num

print("La suma total es:", total_suma)

# Cálculo del Promedio (for)
numeros_promedio = [10, 15, 20, 25, 30]
suma_numeros = 0
cantidad_numeros = 0

for num in numeros_promedio:
    suma_numeros += num
    cantidad_numeros += 1

promedio_final = suma_numeros / cantidad_numeros
print("El promedio es:", promedio_final)

# Filtrando números mayores que un valor (For)
lista_numeros = [5, 25, 12, 33, 18, 45, 7]

limite = int(input("Ingresa un número umbral: "))

for valor in lista_numeros:
    if valor > limite:
        print(valor)

# Búsqueda de un valor específico (for, booleano)
numeros_busqueda = [9, 41, 12, 3, 74, 15]
hallado = False

for valor in numeros_busqueda:
    if valor == 3:
        hallado = True
        break

print("El valor 3 fue encontrado:", hallado)

# Encontrando el número menor (for y None)
numeros_menor = [30, 10, 5, 25, 50, 2]
menor_actual = None

for valor in numeros_menor:
    if menor_actual is None:
        menor_actual = valor
    elif valor < menor_actual:
        menor_actual = valor

print("El número más pequeño es:", menor_actual)
