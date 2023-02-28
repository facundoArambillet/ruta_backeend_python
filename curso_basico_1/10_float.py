x = 3.3
y = 1.1 + 2.2

print(x == y)

y_str = format(y, ".2g")

print(y_str)
print(y_str == str(x))

print("*" * 50)
print(x)
print(round(y,1) == x)

x = 3.3
y = 1.1 + 2.2
y_str = format(y, ".2g")
y_str_v2 = round(y,1)