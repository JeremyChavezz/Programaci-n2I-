with open("mboxs.txt", "r") as archivo:
    numeros = [float(linea) for linea in archivo]

promedio = sum(numeros) / len(numeros)
print("Promedio:", promedio)
