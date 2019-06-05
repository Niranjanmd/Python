letters = ['a','b','c','d']

for letter in letters: #itirate over List
    print(letter)


for letter in enumerate(letters): # we will get tuple which is read only
    # print(letter[0],letter[1])
    index,val = letter #unpacking Tuple index will go to index and value will be in val
    print(index,val)