# def find_volume(length=1, width=1, depth=1): #Con esto defino que por default esas variables tengan ese valor
#     return length * width * depth            #Por si llaman a la funcion sin pasarle parametros

# result = find_volume() 
# print(result)


def find_volume(length=1, width=1, depth=1):
    return length * width * depth            

result = find_volume(width=10)  #habiendo puesto valores por default puedo mandarle por parametro
print(result)                   #ninguno , uno o algunos valores