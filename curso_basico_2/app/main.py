import utils

def run():
    country = input("Escribe el nombre de el pais: ")

    result = utils.population_by_country(utils.countrys, country.title())


    if(result != []):
        country = result[0].get("country")
        population = result[0].get("population")
        print(f"El pais {country} tiene una poblacion de {population}")
    else:
        print(f"No se encuentra registro de este pais: {country}")

if(__name__ == "__main__" ):  #Con esto controlo que cuando importo este modulo
    run()                     #No se me ejecute todo el codigo y asi poder controlar
                              #Que metodos utilizar desde el otro archivo