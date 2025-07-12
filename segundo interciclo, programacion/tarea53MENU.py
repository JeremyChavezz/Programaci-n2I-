# MENÚ BÁSICO DE ARCHIVOS USANDO with open, split, strip, input y print

def crear_archivo():
    nombre = input("Nombre del archivo (sin extensión): ").strip()
    with open(nombre + ".txt", "w") as archivo:
        archivo.write("")  # crea un archivo vacío
    print("Archivo creado correctamente.")

def escribir_archivo():
    nombre = input("Archivo al que deseas escribir (sin .txt): ").strip()
    try:
        with open(nombre + ".txt", "a") as archivo:
            texto = input("Escribe el contenido: ")
            archivo.write(texto + "\n")
        print("Contenido guardado.")
    except FileNotFoundError:
        print("El archivo no existe. Usa la opción 1 para crearlo primero.")

def eliminar_archivo():
    nombre = input("Archivo a eliminar (sin .txt): ").strip()
    import os
    try:
        os.remove(nombre + ".txt")
        print("Archivo eliminado.")
    except FileNotFoundError:
        print("El archivo no existe.")

def mostrar_contenido():
    nombre = input("Archivo a leer (sin .txt): ").strip()
    try:
        with open(nombre + ".txt", "r") as archivo:
            lineas = archivo.readlines()
            for i, linea in enumerate(lineas):
                partes = linea.strip().split()
                print(f"Línea {i+1}: {partes}")
    except FileNotFoundError:
        print("El archivo no existe.")

def menu():
    while True:
        print("\n=== MENÚ ===")
        print("1. Crear archivo")
        print("2. Escribir en archivo")
        print("3. Eliminar archivo")
        print("4. Mostrar contenido (usando split y strip)")
        print("5. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            crear_archivo()
        elif opcion == "2":
            escribir_archivo()
        elif opcion == "3":
            eliminar_archivo()
        elif opcion == "4":
            mostrar_contenido()
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida.")

# Iniciar programa
menu()