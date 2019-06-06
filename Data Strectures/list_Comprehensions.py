# list comprohension is used to map and filter the lists
items = [
    ("product70",300),
    ("product2",246),
    ("product55",346),
    ("product6",24)
]


# [expression for item in items] for each item the expression will be given 

prices = [item[1] for item in items]

print(prices)



prices = [item[1] for item in items if item[1] > 100]

print(prices)
