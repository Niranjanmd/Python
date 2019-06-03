Success_Status = True
for number in range(1,4):
    print("Attempt",number)
    if Success_Status:
        print("Successfull")
        break
else:
    print("Attempted 3 Times and Failed") # Execute only if for Loop complete all the itiration 