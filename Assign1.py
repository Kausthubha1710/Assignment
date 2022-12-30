#list
l = []
# Adding Element into list
l.append(3)
l.append("Samsung")
l.append(5.4)
print("Adding 3,5.4,'Samsung' to the list", l)
# Popping Elements from list
l.pop()
print("Popped one element from list", l)
print()
 
# Set
s = set()
# Adding element into set
s.add(4)
s.add(3.2)
s.add("Realme")
print("Adding 4,3.2,'Realme' to set", s)
 
# Removing element from set
s.remove(4)
print("Removing 4 from set", s)
print()
 
# Tuple
t = tuple(s)
# Tuples are immutable
print("Tuple", t)
print()
 
# Dictionary
d = {}
# Adding the key value pair
d[3] = "Three"
d[6] = 4.8
d[9] = 6
print("Dictionary", d)
# Removing key-value pair
del d[9]
print("Dictionary", d)
