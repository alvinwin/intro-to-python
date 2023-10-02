# store the first 10 letters of the alphabet in a list
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(f'this is the list by default: {alphabet}')

# use a slice to print out the first three letters of the alphabet
first_three_letters = alphabet[0:3]
print(f'these are the first three letters after using slice: {first_three_letters}')

# use a slice to print out any three letters from the middle of your list
middle_three_letters = alphabet[4:7]
print(f'these are the middle three letters after using slice: {middle_three_letters}')

# use a slice to print out any three letters from the middle of your list
large_slice = alphabet[2:-1]
print(f'these is a slice from index 2 to -1: {large_slice}')
