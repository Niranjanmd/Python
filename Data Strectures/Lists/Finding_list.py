numbers = list(range(1,30))

letters = ['a','b','c','d']

print(letters.index('d')) #print in which index d exist if d does not exist it throw error so we should check before checking

if 'g' in letters:  # this will check if g exist in letters
    print(letters.index('g')) 

letters.count('g') # one more way to check if the given ITem exist in the list 