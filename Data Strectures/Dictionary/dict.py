point = {"a": 1, "b": 2}  # declaration
print(point)
print(point["a"])

point_d = dict(x=1, y=2, z=30, a=0)  # using dict to declare dictionary

print(point_d["x"])

if "b" in point_d:  # accessing the Key to avoid exception
    print(point_d["x"])

# one more way to access key if key not exist then it return NONE or we can pass second parameter now it return 0
print(point_d.get("b", 0))

del point_d["x"]

print(point_d)

# Itirating Dict

for key in point_d:
    print(key, point_d[key])

for key, value in point_d.items():
    print(key, value)
