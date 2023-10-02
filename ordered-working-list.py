# start with the list you created in working list
careers = ['spy', 'programmer', 'banker', 'writer', 'teacher', 'manager']

# you are going to print out the list in a number of different orders
# each time you print the list, use a for loop rather than printing the raw list
# print a message each time telling us what order we should see the list in

# print the list in its original order
print('this is the career list in the original order')
for career in careers:
    print(career.title())
 
# print the list in alphabetical order
print('\nthis is the career list in alphabetical order')
for career in sorted(careers):
    print(career.title())

# print the list in its original order
print('\nthis is the career list in the original order')
for career in careers:
    print(career.title())

# print the list in reverse alphabetical order
print('\nthis is the career list in reverse alphabetical order')
for career in sorted(careers, reverse=True):
    print(career.title())

# print the list in its original order
print('\nthis is the career list in the original order')
for career in careers:
    print(career.title())

# print the list in the reverse order from what it started
print('\nthis is the career list in the reverse order from what it started')
for career in reversed(careers):
    print(career.title())

# print the list in its original order
print('\nthis is the career list in the original order')
for career in careers:
    print(career.title())

# permanently sort the list in alphabetical order
#   print it out

print('\nthis is the career list after being permanently sorted in alphabetical order')
careers.sort()
for career in careers:
    print(career.title())

# permanently sort the list in reverse alphabetical order
#   print it out
print('\nthis is the career list after being permanently sorted in reverse alphabetical order')
careers.sort(reverse=True)
for career in careers:
    print(career.title())
