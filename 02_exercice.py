# escribir un programa que muestre por pantalla el resultado de la siguiente operacion:
# ((3 + 2) / (2*5)) ** 2)
print(((3 + 2) / (2*5)) ** 2)

# introducir numero de horas trabajadas y coste por hora y mostrar el salario total
num_horas = int(input("Introduce el numero de horas trabajadas: "))
coste_hora = float(input("Introduce el coste por hora: "))
result = num_horas * coste_hora
print(f"El salario total es {result}")


barras = int(input("Introduce el número de barras de pan no son frescas:"))
precio = 3.49
descuento = 0.6
coste = barras*precio*(1-descuento)
print(f"El coste de una barra fresca es{precio}")
print(f"El descuento sobre una barra no fresca es{descuento*100}")
print(f"El coste finalapagar es{round(coste,2)}")

# Escribir un programa que pida al usuario su peso(en kg)yestatura(en metros),calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es<imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
peso = input("¿Cuál es tu peso en kg ?:")
estatura = input("¿Cuál es tu estatura en metros ?:")
imc_total = float(peso)/float(estatura)**2
imc = round(imc_total, 2)
print(f"Tu índice de masa corporal es{imc}")
