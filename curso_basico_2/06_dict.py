import random

countries = ["arg","br","col","mex"]
population = {country: random.randint(1,100) for country in countries}

population_v2 = { country: population for (country, population) in population.items() if population > 50}
print(population)
print(population_v2)

text = "Hola a todos, esta es una cadena de texto de prueba."
unique = { c: c.upper() for c in text if c in 'aeiou' }


