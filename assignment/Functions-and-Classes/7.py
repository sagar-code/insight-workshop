# 7. Create a list of tuples of first name, last name, and age for your friends
# and colleagues.
# If you don't know the age, put in None.
# Calculate the average age, skipping over any None values.
# Print out each name, followed by old or young if they are above or below the average age.


my_list = [('Shyam', 'Thapa', 40), ('Rabina', 'Karki', 30), ('Gita', 'Sharma', 25)]
age = []

for i in range(len(my_list)):
    age.append(my_list[i][2])

print(age)

avg = sum(age)/len(age)

print("The average age is: {:.2f}".format(avg))

for i in range(len(my_list)):
    if my_list[i][2] > avg:
        print(my_list[i][0] + " is old")
    else:
        print(my_list[i][0] + " is young")