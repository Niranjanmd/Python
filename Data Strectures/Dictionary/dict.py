point = {"x": 1,"y": 1}
print(point)

point_d = dict(x=1,y=2)

point_d["x"]  = 10
point_d["z"] =30

print(point_d)

# check for element before access
if "a" in point_d:
    print(point_d["a"])


# another way to access dict using key

print(point_d.get("a",0))

del point_d["x"]

print(point_d)

#itirate through the list in python 
for key in point_d:
    print(key , point_d[key])

#itirate using items
for key,value in point_d.items():
    print(key,value)



    