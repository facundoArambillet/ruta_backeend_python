def sum_with_range(min,max):
    sum = 0
    for i in range(min,max):
        sum += i
    return sum

result = sum_with_range(1,10)
print(result)