lives = 3
print(type(lives))
temperature = 27.5
print(type(temperature))

number = 45000000000000000.1 #(4.5e+16) Expresa la cantidad de numeros que hay
print(number)                #despues del 45

number = 0.0000000000000000000000000001 #(1e-28) Expresa la cantidad de decimales que hay
print(number)                           # despues del punto



# Ejercicio

enero = input("Ingrese el presupuesto de enero: ")
febrero = input("Ingrese el presupuesto de febrero: ")
marzo = input("Ingrese el presupuesto de marzo: ")
abril = input("Ingrese el presupuesto de abril: ")

promedio = (int(enero) + int(febrero) + int(marzo) + int(abril)) /4
print(f"El promedio es {promedio}") #La f adelante hace lo mismo que las backticks(``) en js y ts