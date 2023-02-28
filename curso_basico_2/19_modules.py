import re  #Regex
import sys #Para saber donde estoy parado
import time #Horas
import collections #Analisis de datos
print(sys.path)

text = "Mi numero de telefono es 36547, los paises son 8931"
result = re.findall("[0-9]+",text)
print(result)

horas = time.localtime()
result = time.asctime(horas)
print(result)


numbers = [1,2,2,3,3,4,4,4,5,5,6,6]
result = collections.Counter(numbers)
print(result)