course = 'Python Programming'

len = len(course)



print(course[0]) #get char in path  ---- p

print(course[-1]) #get the char at the end(last char) ----g

print(course[0:3]) # get from 0th index to 3rd index excluding 3rd index char ---- pyt

print(course[0:-1])  # get from 0th to last index ---- out Python Programmin

print(course[:3])  # get from 0 to index 3 excluding 3rd index char ----pyt

print(course[:]) #print everything


#escape sequence 

# \ is used to escape Sequence

data = "this is some \\\"text\""
print(data)


#String Fromat

first = "Niranjan"
last = "Doreswamy"

print(first+" "+last)

full = f"{first} {last}"  #Inside curly braces we can put any valid expressions

print(full)


# String Methods

stringData = "Python Programming"

print(stringData.upper())  # PYTHON PROGRAMMING

print(stringData)  # python Programming

print(stringData.lower())  # python programming

print(stringData.title())  # python programming

print(stringData.strip()) # remove the space at beginning and end Trim in c# (lstrip to strip at left and rstrip to strip at right)

# value = stringData.index("abc") #throws valueError 

print(stringData.replace('P','J'))

print("pro".upper() in course.upper()) # Check if the character or sequence of character exist in String  ----TRUE
print("Shift".upper() not in course.upper()) # Check if the character or sequence of character exist in String ----TRUE









