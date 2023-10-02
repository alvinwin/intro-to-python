# make a list that includes 4 careers
careers = ['programmer', 'banker', 'writer', 'teacher']

# use the list.index() function to find the index of one career in your list
career_to_find = 'teacher'
career_index = careers.index(career_to_find)

# print index of given career
print(f"The index of '{career_to_find}' is {career_index}")

# use the in function to show that this career is in your list
print('writer is a career in careers')
print('writer' in careers)
print('police is a career in careers')
print('police' in careers)

# use the append() function to add a new career to your list
careers.append('manager')
print(careers)

# use the insert() function to add a new career at the beginning of the list
careers.insert(0, 'spy')
print(careers)

# use a loop to show all the careers in your list
for index, career in enumerate(careers):
    index = str(index)
    print("index " + index + ", career: " + career.title())
