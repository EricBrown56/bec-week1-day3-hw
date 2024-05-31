# Find out which students both submitted their assignments and attended the class.

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

# Create a list of students who both submitted their assignments and attended the class

both = []

for i in submitted:
    if i in attended:
        both.append(i)

print(both)

#---------------------------------------------------------------------------------------

# Check if the two lists are identical regardless of order

check = submitted == attended
print(check)

# These two lists are not identical

#---------------------------------------------------------------------------------------

# Removing a studend from attended if they did not submit their assignment

for i in attended:
    if i not in submitted:
        attended.remove(i)

print(attended)





