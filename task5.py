from functools import reduce

def my_func(a,b):
    return a*b


print(f"Четные значения: {[el for el in range(100,1000) if el % 2 ==0]}")
print(f"Результат произведения: {reduce(my_func,[el for el in range(100,1000) if el % 2 ==0])}")