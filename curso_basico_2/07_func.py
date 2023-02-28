def calculator(number_1,number_2,operation):
    result = 0

    if(operation == "+"):
        result = number_1 + number_2
    elif(operation == "-"):
        result = number_1 - number_2
    elif(operation == "*"):
        result = number_1 * number_2
    elif(operation == "/"):
        if(number_2 == 0 and operation == "/"):
            print("No se puede dividir por 0")
        else:
            result = number_1 / number_2
    print(result)

calculator(5,0,"/")