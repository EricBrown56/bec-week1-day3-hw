# Extracting a list of elements from a list using slicing

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

# Extract the second week of temperatures

week2 = temperatures[7:14]
print(week2)

#-----------------------------

# Extract all temperatures above 100 degrees

above_100 = temperatures[-6:]
print(above_100)

#-----------------------------

# Reverse the list and extract the 5th through 10th days of the reversed list

temperatures.reverse()

reversed_extract = temperatures[4:10]
print(reversed_extract)

#-----------------------------

