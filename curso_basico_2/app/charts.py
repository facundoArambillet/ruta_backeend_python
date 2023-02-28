import matplotlib.pyplot as plt
# import matplotlib.pyplot
user_keys = []
user_values = []
def generate_bar_chart(labels,values):
    # labels = ["a","b","c"]
    # values = [100,200,300]
    ax = plt.subplot()
    ax.bar(labels,values)
    plt.show()

def generate_pie_chart(labels,values):
    # labels = ["a","b","c"]
    # values = [100,200,300]
    ax = plt.subplot()
    ax.pie(values,labels=labels)
    ax.axis("equal")
    plt.show()

def inputs_user():
    user_lenght = int(input("Ingrese la cantidad de variables: "))
    for element in range(user_lenght):
        user_key = input("Ingrese nombre para su variable: ")
        user_keys.append(user_key)
        user_value = int(input("Ingrese el valor de su variables: "))
        user_values.append(user_value)
    

if __name__ =="__main__":
    inputs_user()
    generate_bar_chart(user_keys,user_values)
    generate_pie_chart(user_keys,user_values)