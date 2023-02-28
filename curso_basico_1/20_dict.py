person = {
    "name": "Facundo",
    "last_name": "Arambillet",
    "age": 24,
    "langs": ["python","javascript","typescript"]
}
person["name"] = "Clemente"
person["langs"].append("HTML")
print(person)
print("*" * 90)
del person["last_name"]
print(person)
print("*" * 90)
print(person.items())
print("*" * 90)
print(list(person.keys()))  #CON EL METODO "list" LO DEVUELVE EN FORMA DE ARRAY
print("*" * 90)
print(person.values())