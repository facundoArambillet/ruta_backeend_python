# union(set):
# Realiza la operacion “union” entre dos conjuntos.
# La unión entre dos conjuntos es sumar los elementos de estos sin repetir elementos. 
# Esta operación tambien se puede realizar con el signo “|”: set_a | set_b.
# intersection(set): Realiza la operacion “intersection” entre dos conjuntos.
#  La intersección entre dos conjuntos es tomar unicamente los elementos en común de los conjutnos.
# Esta operación tambien se puede realizar con el signo “&”: set_a & set_b.
# difference(set): Realiza la operacion “difference” entre dos conjuntos. 
# La diferencia entre dos conjuntos es restar los elementos del segundo conjunto
# al primero. Esta operación tambien se puede realizar con el signo “-”: set_a - set_b.
# symmetric_difference(set): Realiza la operacion “symmetric_difference” entre dos conjuntos. 
# La diferencia simetrica entre dos conjutnos consta de restar todos los elementos de ambos 
# exceptuando el elemento en común. Esta operación
# tambien se puede realizar con el signo “^”: set_a ^ set_b.


set_a = {"col","mex","bol"}
set_b = {"arg","brasil","bol"}

# UNION
set_c = set_a.union(set_b)
print(set_c)
# print(set_a | set_b) #Hace lo mismo sin necesidad de llamar al metodo "union"

# INTERSECCION
set_c = set_a.intersection(set_b) #Retorna el elemento repetido
print(set_c)
# print(set_a & set_b) #Hace lo mismo sin necesidad de llamar al metodo "intersection"

# DIFERENCIA
set_c = set_a.difference(set_b) #Resta el segundo conjunto al primero
print(set_c)
# print(set_a - set_b) #Hace lo mismo sin necesidad de llamar al metodo "difference"

# DIFERENCIA SIMETRICA
set_c = set_a.symmetric_difference(set_b) #Hace una union sacando los elementos repetidos
print(set_c)
# print(set_a ^ set_b) #Hace lo mismo sin necesidad de llamar al metodo "symmetric_difference"