letters = ['a','b','c','d']

#add
letters.append('f') # add at last

letters.insert(2,'ab') #insert to specific index

print (letters)

#remove
letters.pop() #remove last letter

removed = letters.pop(2) #remove from given index and give the removed value 
print(removed)

letters.remove("b") #remove the first element given


del letters[0:2]  #using del we can remove range of elements from list 


print(letters)