temp = 20 #input('Temprature : ')

if int(temp) > 30:
    print('Its Warm')
    print('drink Water')
elif int(temp)>20:
    print('Nice Temp')
else:
    print('its cold')

print("Done")

#Ternary operation 

age = 15

message = "Eligible" if age > 18 else "Not Eligible"

print(message)