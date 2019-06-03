INPUT = input("ENter the range")
i = 0
for n in range(1, int(INPUT)+1):
    if n % 2 == 0:
        print(n)
        i+=1

print(f"we have {i} even numbers")
