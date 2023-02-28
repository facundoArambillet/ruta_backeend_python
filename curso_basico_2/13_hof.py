high_ord_func = lambda x,func: x + func(x)

increment = lambda x: x + 2

result = high_ord_func(2,increment) #Puedo pasarle una funcion de parametro
print(result)                        #en este caso es "increment"


result = high_ord_func(2,lambda x: x + 2) #Tambien puedo pasar el codigo directamente
print(result)                              #Sin necesidad de crear una funcion