##from itertools import count
##for el in count(int(input("Введите число "))):
##    print(el)

from itertools import cycle

my_list = [123, 33]
for el in cycle(my_list):
    print(el)