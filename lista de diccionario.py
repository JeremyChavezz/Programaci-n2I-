# 1. Crear una lista con al menos 5 elementos e imprimir cada uno con su índice
frutas = ["manzana", "banana", "naranja", "pera", "uva"]
for i, fruta in enumerate(frutas):
    print(f"Índice {i}: {fruta}")

print("\n" + "-"*50 + "\n")

# 2. Pedir al usuario varias palabras, guardarlas en una lista y mostrar la más larga
palabras = input("Ingresa varias palabras separadas por espacio: ").split()
palabra_mas_larga = max(palabras, key=len)
print(f"La palabra más larga es: {palabra_mas_larga}")

print("\n" + "-"*50 + "\n")

# 3. Contar la frecuencia de palabras en una línea de texto
linea = input("Ingresa una línea de texto: ")
frecuencia = {}
for palabra in linea.split():
    palabra = palabra.lower().strip(".,!?")  # limpiar signos
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

print("Frecuencia de palabras:")
for palabra, conteo in frecuencia.items():
    print(f"{palabra}: {conteo}")

print("\n" + "-"*50 + "\n")

# 4. Leer un archivo de texto `datos.txt` y mostrar las 3 palabras más repetidas
from collections import Counter

try:
    with open("datos.txt", "r", encoding="utf-8") as archivo:
        contenido = archivo.read().lower()
        palabras = contenido.split()
        palabras = [p.strip(".,!?") for p in palabras]
        conteo = Counter(palabras)
        mas_comunes = conteo.most_common(3)
        print("Las 3 palabras más repetidas son:")
        for palabra, cantidad in mas_comunes:
            print(f"{palabra}: {cantidad}")
except FileNotFoundError:
    print("El archivo 'datos.txt' no fue encontrado.")

print("\n" + "-"*50 + "\n")

# 5. Simular una tienda con diccionarios: productos y precios, y permitir búsquedas
tienda = {
    "camisa": 15.99,
    "pantalón": 25.50,
    "zapatos": 45.00,
    "gorra": 8.75,
    "chaqueta": 60.00
}

print("Productos disponibles:")
for producto, precio in tienda.items():
    print(f"{producto.title()}: ${precio}")

buscar = input("\n¿Qué producto deseas buscar? ").lower()
if buscar in tienda:
    print(f"{buscar.title()} cuesta ${tienda[buscar]}")
else:
    print("Producto no encontrado.")
