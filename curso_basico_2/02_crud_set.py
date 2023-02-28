# add(): Añade un elemento.
# update(): Añade cualquier tipo de objeto iterable como: listas, tuplas.
# discard(): Elimina un elemento y si no existe no lanza ningún error.
# remove(): Elimina un elemento y si este no existe lanza el error “keyError”.
# pop(): Nos devuelve un elemento aleatorio y lo elimina y si el conjunto está vacío lanza el error “key error”.
# clear(): Elimina todo el contenido del conjunto.


set_countries = {"arg","col","mex"}

print("arg" in set_countries) #El "in" indica si el primer argumento esta dentro del segundo


set_countries.update({"bol","peru"}) #Puedo aregar varios a la vez o uno solo(add())

print(set_countries)