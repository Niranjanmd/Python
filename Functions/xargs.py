def multiply(*numbers):
    res = 1
    for num in numbers:
        res = res * num
    return res


print(multiply(2,2,2))


#xxargs
#when we use **args then we can pass multiple keyvalued args and python compier will build a dictionary 

def printUser(**user):
    print(user)

printUser(id=1,name="Niranjan",age=28)

