text = "El sabe programar en Python"
print("JavaScript" in text) #te devuelve si la palabra esta o no dentro de algo

size = len(text) #Te devuelve la cantidad de caracteres de la variable que le metas
print(size)

text_upper = text.upper() #Lo pasa a mayusculas
text_lower = text.lower() #Lo pasa a minusculas
print(text_upper)
print(text_lower)

text_count = text.count("El") #Devuelve la cantidad del caracter que le pases dentro  de la variable que le pases
print(text_count)

text_start = text.startswith("El") #Boleean para ver si empieza con la variable que le pases
text_end = text.endswith("El") #Boleean para ver si termina con la variable que le pases

text_replace = text.replace("Python","JavaScript") #Boleean para ver si empieza con la variable que le pases

text_capitalize = text.capitalize() #Pasa todo a minusculas menos la primera letra
text_isdigit = text.isdigit() #Te devuelve si es o no un digito