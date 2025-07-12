# Copiar el contenido de un archivo a otro
with open("mbox.txt","r") as origen:
    contenido = origen.read()

with open("copia.txt", "w") as copia:
    copia.write(contenido)
