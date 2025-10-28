from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, parent, grandparent')

# Define parent relationships (facts)
+parent('Alice', 'Bob')
+parent('Bob', 'Charlie')
+parent('Charlie', 'David')

# Define rule: if X is parent of Y and Y is parent of Z, then X is grandparent of Z
grandparent(X, Z) <= parent(X, Y) & parent(Y, Z)

# Query: Who are Alice's grandchildren?
print(grandparent('Alice', Y))
