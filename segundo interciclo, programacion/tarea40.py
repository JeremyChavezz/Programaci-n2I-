# Leer el archivo archivo.txt
with open("ambox.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        print(linea.strip())