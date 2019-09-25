# Generator are like list but they dont store all the element in memory they generate the items on each Itiration
from sys import getsizeof

numbers = [x for x in range(10)]

generator = (x for x in range(10))

print(generator)  # This is generator not a ist
# for gen in generator:
#     print(gen)

print("GEN: ", getsizeof(generator))  # this will be same even if the range will be 1000
print("List: ", getsizeof(numbers))  # this will be same even if the range will be 1000
