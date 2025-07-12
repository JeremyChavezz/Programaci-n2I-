lineas = ["Hola, mundo\n", "Este es un archivo de prueba\n", "Python es genial\n"]

with open("mbox.txt", "w", encoding="utf-8") as archivo:
    archivo.writelines(lineas)