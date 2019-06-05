letters = ['z','d','r','g','q']

# letters.sort()  # this will modifi the list 

# print(letters)

# print(sorted(letters)) # this will return new list original will not be modified
# print(letters)


items = [
    ("product70",300),
    ("product2",246),
    ("product55",346),
    ("product6",24)
]


print(items)
def sort_item(item):
    print(item[0])
    return item[0]

# items.sort(key = sort_item) #using function

items.sort(key=lambda x:x[1]) #using lambda



print(items) 