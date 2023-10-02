# make a list of 5 numbers, in a random order

# import library random
import random

# create a list of numbers 1-5
numbers_list = [1, 2, 3, 4, 5]

# shuffle numbers_list to generate a list with a random order
random.shuffle(numbers_list)

# test randomly generated list  
print(numbers_list)

# you are going to print out the list in a number of different orders
# print a message each time telling us what order we should see the list in

print('\nbelow is the list of numbers printed in the original order')
for number in numbers_list:
	print(number)

print('\nbelow is the list of numbers printed in increasing order')
for number in sorted(numbers_list):
	print(number)

print('\nbelow is the list of numbers printed in the original order')
for number in numbers_list:
	print(number)

print('\nbelow is the list of numbers printed in decreasing order')
for number in sorted(numbers_list, reverse=True):
	print(number)

print('\nbelow is the list of numbers printed in the original order')
for number in numbers_list:
	print(number)

print('\nbelow is the list of numbers printed in reverse order')
for number in reversed(numbers_list):
	print(number)

print('\nbelow is the list of numbers printed in the original order')
for number in numbers_list:
	print(number)

print('\npermanently sort the numbers in increasing order, then print them out')
numbers_list.sort()
for number in numbers_list:
	print(number)

print('\npermanently sort the numbers in increasing order, then print them out')
numbers_list.reverse()
for number in numbers_list:
	print(number)
