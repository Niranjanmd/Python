#Ways to create lists 

letters = ["a","b","c"]

matrix = [[0,1],[2,3]]

matrixMul = matrix * 3 # to repeat the element in the list

print(matrixMul)  # [[0, 1], [2, 3], [0, 1], [2, 3], [0, 1], [2, 3]]

zeros = [0] * 5 
 
print(zeros)  # [0, 0, 0, 0, 0]

combined = zeros + letters #concatination

print(combined)  #  [0, 0, 0, 0, 0, 'a', 'b', 'c']

numbers = list(range(1, 11))  

print(numbers)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

chars = list("Hello World")

print(chars)

print(len(chars))



