def fuzz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        return 'fizz_buzz'
    elif input % 5 == 0:
        return 'buzz'
    elif input % 3 == 0:
        return 'fizz'
    else:
        return input


val = input("Enter Val :")

print(fuzz_buzz(int(val)))
