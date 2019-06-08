# Tuple is basically a readonly list we can not modify the tuple once created

point = 1 , 2

print(point)

print(type(point))

tupledata = tuple([1,30,'abc'])

print(tupledata)

print(type(tupledata))

point = "abc",

print(point)


# swapping 

x =1 
y = 2

x , y = y , x  # we are unpacking tuple y,x is considerd as tuple and 

a,b = 1 , 2 # above and this are same

print(x,y)