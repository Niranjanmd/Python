numbers = list(range(4))

first,second,third,four = numbers

print(first)

f,s,*o= numbers # If we want only first 2 elements
print(f, s)
print(o)

f, *o, s = numbers  # If we want only first and last elements

print(f,s)
print(o)

