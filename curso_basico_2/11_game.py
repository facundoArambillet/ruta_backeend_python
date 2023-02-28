import random

computer_option = ["piedra", "papel", "tijera"]

def numero_aletarorio(minimo, maximo):
    # randint sirve para generar un numero entre un minimo y un maximo
    return random.randint(minimo, maximo)


num = numero_aletarorio(0, (len(computer_option)-1))


def game():
    user_option = input("Elija piedra, papel o tijera: ").lower()
    
    while not user_option in computer_option:
        print("Valor invalido porfavor vuelva a elegir un valor")
        user_option = input("Elija piedra, papel o tijera: ").lower()

    if (user_option == computer_option[num]):
        print(f"Computadora eligio: {computer_option[num]}")
        print("Hay un empate!")
    elif (user_option == "piedra" and computer_option[num] == "tijera"):
        print(f"Computadora eligio: {computer_option[num]}")
        print("Felicitaciones ganaste!")
    elif (user_option == "papel" and computer_option[num] == "piedra"):
        print(f"Computadora eligio: {computer_option[num]}")
        print("Felicitaciones ganaste!")
    elif (user_option == "tijera" and computer_option[num] == "papel"):
        print(f"Computadora eligio: {computer_option[num]}")
        print("Felicitaciones ganaste!")
    else:
        print(f"Computadora eligio: {computer_option[num]}")
        print("Lo siento perdiste!")

game()