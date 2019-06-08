# its a collection with no duplicates
# Item in set is not sequential that is we can use index to access them number[0] will throw error
numbers = [1, 2, 3, 4, 5, 1, 2, 3, 2, 1]

first = set(numbers)

second = {2, 4, 10}

# second.add(4)

# second.remove(2)

print(len(second))

print(first)

print("Union", first | second)

print("Intersection", first & second)

print("only In First :", first - second)

print("Either in first or second and not both : ", first ^ second)
