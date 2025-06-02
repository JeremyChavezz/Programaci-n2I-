# 1. Crear una función que imprima un mensaje 
def saludo():
    print('¡Hola, mundo!')

# 2. Función con un argumento
def saludar(usuario):
    print(f'Hola, {usuario}')

# 3. Suma de dos números
def sumar(x, y):
    return x + y

# 4. Calcular el salario
def computepay(h, t):
    if h > 40:
        e = h - 40
        return 40 * t + e * t * 1.5
    else:
        return h * t

# 5. Función para determinar el mayor carácter
def mayor_caracter(texto):
    return max(texto)

# 6. Conversión de tipo
def convertir_a_flotante(dato):
    try:
        return float(dato)
    except ValueError:
        return None

# 7. Función que retorna un saludo en diferentes idiomas
def saludo_idioma(codigo):
    if codigo == 'es':
        return 'Hola'
    elif codigo == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

# 8. Comprobar si un número es par
def es_par(n):
    return n % 2 == 0

# 9. Concatenar cadenas
def concatenar(a, b):
    return a + b

# 10. Calcular promedio
def promedio(datos):
    if len(datos) == 0:
        return 0
    return sum(datos) / len(datos)

# 11. Contar vocales
def contar_vocales(texto):
    v = 'aeiouAEIOU'
    return sum(1 for letra in texto if letra in v)

# 12. Revertir cadena
def invertir(palabra):
    return palabra[::-1]

# 13. Tabla de multiplicar
def tabla(base):
    for n in range(1, 11):
        print(f'{base} x {n} = {base * n}')

# 14. Función sin parámetros
def mensaje():
    print("Primera línea")
    print("Segunda línea")
    print("Tercera línea")

# 15. Función que retorne el número más pequeño
def menor_valor(valores):
    return min(valores)

# 16. Calcular factorial
def factorial(valor):
    if valor < 0:
        return None
    res = 1
    for i in range(1, valor + 1):
        res *= i
    return res

# 17. Determinar si un número es primo
def es_primo(num):
    if num < 2:
        return False
    for div in range(2, int(num ** 0.5) + 1):
        if num % div == 0:
            return False
    return True

# 18. Repetir una cadena n veces
def repetir(txt, veces):
    return txt * veces

# 19. Función con múltiples parámetros
def descripcion(persona, años, lugar):
    print(f'{persona} tiene {años} años y vive en {lugar}.')

# 20. Verificar palíndromo
def es_palindromo(texto):
    texto = texto.lower().replace(" ", "")
    return texto == texto[::-1]
