import functools

def accum(counter,item):

    return counter + item

numbers = [1,2,3,4,5]
#result = functools.reduce(lambda counter,number: counter + number, numbers)
result = functools.reduce(accum, numbers)

print(result)