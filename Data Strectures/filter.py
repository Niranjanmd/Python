items = [
    ("product70",300),
    ("product2",246),
    ("product55",346),
    ("product6",24)
]


priceGreater_100 = list(filter(lambda x : x[1] > 100,items))

print(priceGreater_100)