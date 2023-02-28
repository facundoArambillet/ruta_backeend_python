# try:
#     print(0/0)
# except ZeroDivisionError as error:
#     print(error)

user_age = int(input("Ingrese su edad: "))
def discotheque(age):
    try:
        if(age > 18):
            print("Bienvenido al boliche")
        else:
            raise Exception("No se permiten menores de edad")
    except Exception as error:
        print(error)    

discotheque(user_age)

