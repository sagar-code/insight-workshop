# 4. Create a list.
# Append the names of your colleagues and friends to it.
# Has the id of the list changed?
# Sort the list. What is the first item on the list?
# What is the second item on the list?

list_of_names = []

print(f"Empty list has been created, with id: {id(list_of_names)} and value {list_of_names}")

list_of_names.append('Sagar')
list_of_names.append('Hari')
list_of_names.append('Shyam')

print("Few name were added to the above list.")
print(f'value: {list_of_names}\nId: {id(list_of_names)}')
print('Sorting the list...')

list_of_names.sort()

print(f'Sorted list has {list_of_names[0]} and {list_of_names[1]} names on first two indices.')