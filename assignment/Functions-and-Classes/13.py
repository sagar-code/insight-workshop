# 13. Write a function to write a comma-separated value (CSV) file. It
# should accept a filename and a list of tuples as parameters. The
# tuples should have a name, address, and age. The file should create
# a header row followed by a row for each tuple. If the following list of
# tuples was passed in:
# [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave',
# 21)] it should write the following in the file:
# name,address,age
# George,4312 Abbey Road,22
# John,54 Love Ave,21


import csv


def csv_file(filename, my_tuple):
    fields = ['Name', 'Address', 'Age']
    # writing to csv file
    with open(filename, 'w') as file:
        # creating a csv writer object
        writer = csv.writer(file)
        writer.writerow(fields)
        writer.writerows(my_tuple)


csv_file('peoples_record.csv', [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21),
                                      ('Paul', '2020 Park Ave', 23)])