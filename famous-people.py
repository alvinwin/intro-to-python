# make a list that includes the name of four famous people
famous_people = ['Alan Turing', 'Ada Lovelace', 'Aristotle', 'Vincent van Gogh']
print(f'\nhere is the list by default {famous_people}')
# remove each person from the list, one at a time, using each of the four methods we have just seen

# pop the last item from the list
popped_person = famous_people.pop()
print(f'\nthis is the removed famous person: {popped_person}')
print(f'\nthis is the list after {popped_person} was removed: {famous_people}')

# pop any item except the last item
popped_2 = famous_people.pop(0)
print(f'\nthis is the second removed famous person: {popped_2}')
print(f'\nthis is the list after {popped_2} was removed: {famous_people}')

# remove one item by its position
fp_tobedeleted = famous_people[1]
print(f'\nthis is the third removed famous person: {famous_people[1]}')
del famous_people[1]
print(f'\nthis is the list after {fp_tobedeleted}  was removed: {famous_people}')

# one item by its value
fp_tobedeleted = famous_people[0]
print(f'\nthis is the fourth removed famous person: {fp_tobedeleted}')
famous_people.remove('Ada Lovelace')
print(f'\nthis is the list after {fp_tobedeleted}  was removed: {famous_people}')

