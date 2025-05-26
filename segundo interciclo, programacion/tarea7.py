def computepay(horas, tarifa):
    if horas > 40:
        horas_extras = horas - 40
        salario = 40 * tarifa + horas_extras * (tarifa * 1.5)
    else:
        salario = horas * tarifa
    return salario

# Datos de entrada
horas = 45
tarifa = 10

# Cálculo del salario
salario = computepay(horas, tarifa)

# Mostrar resultado
print("Salario:", salario)