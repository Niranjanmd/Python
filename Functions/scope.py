message = "a"  #global 

def greet():
    global message  #This line will be used to tell compiler that you need to change value of global message
    message = "b"  #with out above line this will be local variable and does not change value of global message

print(message)

greet()

print(message)