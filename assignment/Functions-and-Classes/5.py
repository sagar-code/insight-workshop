# 5. Create a tuple with your first name, last name, and age.
# Create a list, people, and append your tuple to it.
# Make more tuples with the corresponding information from your friends and append them to the
# list.
# Sort the list.
# When you learn about sort method, you can use the
# key parameter to sort by any field in the tuple, first name, last name,
# or age.


# creating tuple
my_tuple = ('Sagar', 'Budhathoki', 22)

# creating list
people = []
people.append(my_tuple)
print(people)

t1 = ('Shyam', 'Thapa', 23)
t2 = ('Rabina', 'Karki', 21)

people.extend([t1, t2])

print(people)

# sorting tuple by age field
sorted_list = sorted(people, key=lambda tup: tup[2])

print(sorted_list)