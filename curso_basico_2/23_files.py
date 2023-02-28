file = open("./file.txt")
print(file.read())
print(file.readline())
print(file.readline())

file.close() #Cierra el archivo liberando espacio en memoria

with open("./file.txt") as file:    #Lo cierra ni bien termina de ejecutarlo
    for line in file:               
        print(line) 