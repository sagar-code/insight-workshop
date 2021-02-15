# 34. Write a Python script to merge two Python dictionaries.

d1 = {1: 'a', 2: 'b'}
d2 = {3: 'c', 4: 'd'}

result = {**d1, **d2}
print(result)

d = d1.copy()
d.update(d2)
print(d)