import csv
import re
import app.charts 
def read_csv(path):
    with open(path,"r") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        header = next(reader)
        data = []
        populations = {}
        country_user = input("Escribe el nombre del pais: ")
        for row in reader:
            iterable = zip(header,row)
            country_dict = {key: value for key,value in iterable}
            if(country_dict.get("Country/Territory") == country_user.title()):
                data.append(country_dict)
            
                for key,value in data[0].items():
                    if(r"Population") in key:
                        regex = r"\D*"
                        populations[re.sub(regex,"",key)] = float(value)
                #print(data[0].items())       
               # print("***" * 33)
        populations.pop("")
       #print(populations)
        return data,populations

if __name__ == "__main__":
    data = read_csv("./app/data.csv")
    country = data[0]
    country_population = data[1]
    print(country)
    print("*****"*17)
    print(country_population)
    country_keys = list(country_population.keys())
    country_keys.reverse()
    country_values = list(country_population.values())
    country_values.reverse()
    app.charts.generate_bar_chart(country_keys,country_values)