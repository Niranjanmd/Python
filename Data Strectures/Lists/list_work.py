#append,insert, pop, del, 

letters = ["a", "b", "c","d","e","f"]

letters.append("G")

print(letters[1])

print(letters)

# del letters[2] #dleete the value at the given index

# print(letters)

# letters.pop(2)  # remove the elemet given index and retrun the removed value

print(letters)

print(letters[::2])   # ['a', 'c', 'e', 'G']


numbers = list(range(20))

print(numbers[::-1]) # print all the element in reverse order
