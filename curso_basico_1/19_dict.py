my_dict = {} #Los diccionarios son lo mismo que los JSON

my_dict = {
    "name": "Facundo",
    "last_name": "Arambillet",
    "age": "24",
}
print(my_dict.get("name")) #Con get me devuelve none si no existe la variable que le paso

print("name" in my_dict)
print("avion" in my_dict)