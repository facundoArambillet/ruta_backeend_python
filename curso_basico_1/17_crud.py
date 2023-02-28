# append(): Añade un ítem al final de la lista.
# clear(): Vacía todos los ítems de una lista.
# extend(): Une una lista a otra.
# count(): Cuenta el número de veces que aparece un ítem.
# index(): Devuelve el índice en el que aparece un ítem (error si no aparece).
# insert(): Agrega un ítem a la lista en un índice específico.
# pop(): Extrae un ítem de la lista y lo borra.
# remove(): Borra el primer ítem de la lista cuyo valor concuerde con el que indicamos.
# reverse(): Le da la vuelta a la lista actual.
# sort(): Ordena automáticamente los ítems de una lista por su valor de menor a mayor.

numbers = [1,2,3,4,5]
numbers.append(750)
print(numbers)

numbers.insert(0,100) #Crea un nuevo elemento en una posicion espeficia corriendo lo demas a la derecha
print(numbers)

tasks = ["hola 1","hola 2","hola 3"]

new_list = numbers + tasks #Se pueden fusionar arrays
print(new_list)