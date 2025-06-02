def juego_numero_secreto():
    numero_secreto = 56
    num = int(input("Adivina el número secreto (entre 1 y 100): "))
    while num != numero_secreto:
        if num < numero_secreto:
            print("El número es mayor")
        else:
            print("El número es menor")
        num = int(input("Dame un número: "))
    print("¡Felicidades! ¡Ganaste!")
juego_numero_secreto()