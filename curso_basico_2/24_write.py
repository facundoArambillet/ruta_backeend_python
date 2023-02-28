with open("./file.txt","r+") as file:    
    for line in file:               
        print(line) 
    file.write("\nNueva linea")