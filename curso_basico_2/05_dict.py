import random

dict = {element: element * 2 for element in range(1,5)}
print(dict)

countries = ["arg","br","col","mex"]
population = {}

for country in countries:
    population[country] = random.randint(1,1000)

print(population)


names = ["facundo","clemente","heroel"]
ages = [24,25,29]

print(list(zip(names,ages)))
new_dict = {name: age for(name,age) in zip(names,ages)}
print(new_dict)

