items = [
    ("product70",300),
    ("product2",246),
    ("product55",346),
    ("product6",24)
]


prices = [
]

for item in items:
    prices.append(item[1])

print(prices)

y = map(lambda x:x[1],items)

for i in y:
    print(i)

#to create list directly

doublePrices = list (map(lambda x : x[1] * 2 , items ))

print(doublePrices)


