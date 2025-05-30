# Python List Basics


# Generate a List without data
a = []

# Or generate a List with some data
b = [10, 20, 30, 40, 50]


# Extract a specific data in a list via index
print(b[0]) # Got 10
print(b[1]) # Got 20
print(b[2]) # Got 30
print(b[3]) # Got 40
print(b[4]) # Got 50

# The above script can be simplified through loop structure
for i in range(5):
	print(b[i], end = ' ')
print()

# or
for i in b:
	print(i, end = ' ')
print()


# Add data at the tail of the list
b.append(60)
print(b) # Got [10, 20, 30, 40, 50, 60]

# Add data at a specific position of the list
b.insert(2, 25)
print(b) # Got [10, 20, 25, 30, 40, 50, 60]


# Remove data in the list
b.remove(30)
print(b) # Got [10, 20, 25, 40, 50, 60]

# Remove data at a specific position of the list
b.pop(0)
print(b) # Got [20, 25, 40, 50, 60]


# Delete data in the list
del b[4]
print(b) # Got [20, 25, 40, 50]

# Attention
del b
print(b) # There is no list b anymore

