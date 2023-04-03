# add elements to set
data = {'a','b','c'}
data.add('d')
print(data)

# delete elements

data.discard('d')
print(data)

# intersection of sets

v1 = {1,2,3,4,45,2,4,61,}
v2 = {45,61}
v3 = v1.intersection(v2)
print(v3)

# union
v4 = v1.union(v2)
print(v4)

# difference
d1 = v1.difference(v2)
print(d1)

