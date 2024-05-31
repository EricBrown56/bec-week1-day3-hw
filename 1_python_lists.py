# Sort grades in decending order

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

grades.sort(reverse=True)

print(grades)

#------------------------------------------------------------

# Calculate the average of the grades

average = sum(grades) / len(grades)

print(average)

#------------------------------------------------------------

# Replace any grade below 80 with the value 'Failed'

for i in grades:
    if i < 80:
        grades[grades.index(i)] = 'Failed'
print(grades)