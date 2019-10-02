from timeit import timeit

code1 = """
def caluclate_xfactor(age):
    if(age <= 0 ):
        raise ValueError("Age can not be 0 or less")
    return 10/age

try:
    caluclate_xfactor(0)
except ValueError as ex:
    pass
"""

code2 = """
def caluclate_xfactor(age):
    if(age <= 0 ):
        return None
    return 10/age

x_fac = caluclate_xfactor(0)

if x_fac == None:
    pass
"""

print("First Code = ",timeit(code1,number=10000))
print("Secon Code = ",timeit(code2, number=10000))
