from package.mod_1 import func_1
from package import mod_1
import package.mod_1, package.mod_2 #Esta es buena practica
print(mod_1.func_1())  #Diferentes maneras de importar
print(func_1())
print(package.mod_1.func_1())

