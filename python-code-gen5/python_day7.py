# Set : store unique value

# empty set
# student = set()

# Avoid duplicate
classroom = {101, "Data Structure", "JomNum-Tech"}
classroom.add("Python")
classroom.add("Data Science")
classroom.add(50)
classroom.add(50)
classroom.remove(101)
classroom.discard(10)

# Union 

a = {1,2,3}
b = {4,5,6}
d = {7,8,9}

# c = b.union(a)
c = b | a | d

# Intersection 

a = {1,2,4,6}
b = {2,3,4,6}

# e = a.intersection(b)
e = a & b

# Difference

i = {1,2,3,4,5}
j = {1,2,3,4,5,6,7} 

# k = i.difference(j)
k = j - i

print(k)