# Reemplaza todas las ocurrencias de "gato" por "perro"
with open("mbox.txt", "r") as archivo:
    contenido = archivo.read()

contenido_modificado = contenido.replace("gato", "perro")

with open("mbox.txt", "w") as archivo:
    archivo.write(contenido_modificado)
