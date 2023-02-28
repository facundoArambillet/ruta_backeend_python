# for element in range(5):  #Empieza en el 0 como los arrays aunque puedo
#     print(element)        #ponerle otro argumento y elegir desde donde empezar
                            # EJ: range(1,5)
my_list = [1,2,3,4,5,6,7,8,9,10]

for i in my_list:
    print(i)

my_tuple = ("Facundo","Juan","Clemente","Federico","Heroel")

for i in my_tuple:
    print(i)

product = {
    "name": "camisa",
    "price": 100,
    "stock": 25,
}

# for key in product:
#     print(f"{key}: {product[key]}")  ES LO MISMO QUE EL METODO DE ABAJO

for key,value in product.items():
    print(f"{key}: {value}") 
