try:
    age = int(input("AGE : "))
    xfactor = 100/age
except (ValueError, Exception) as e:  # e is the execption variable not default
    print("You did not enter the correct age")
    print(e)
else:
    print(age)
finally:
    print("this execute always used for clean up ")

print("execution goes fine ")

