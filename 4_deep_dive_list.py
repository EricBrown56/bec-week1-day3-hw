# Deep dive into python lists

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]



# finding the failing grade and giving it a variable

for x in grades:
    if x < 80:
        failed = x

# Find the index of the failing grade from the grades list and pull that index from the students and activities list

i = failed

index = grades.index(i) # this will return the index of 2, which is the failing grade

print(students[index], grades[index], activities[index])

#---------------------------------------------------------------------------------------

# Another way to do this is to use the zip() function to combine the three lists into a single list of tuples, and then iterate through the zipped list to find the failing grade.

# Create a list of students who have grades below 80 and display their name, grade, and activity
# Use the zip() function to combine the three lists
# Use a for loop to iterate through the zipped list
# Use an if statement to check if the grade is less than 80
# Print the student's name, grade, and activity

# What is the zip function and how does it work?
# The zip function takes two or more lists and combines them into a single list of tuples.
# Each tuple contains the corresponding elements from the input lists.
# If the input lists are of different lengths, the resulting list will have the length of the shortest input list (the excess elements are ignored).
# For example, zip([1, 2, 3], ['a', 'b', 'c', 'd']) will return [(1, 'a'), (2, 'b'), (3, 'c')].
# reference: https://www.w3schools.com/python/ref_func_zip.asp#:~:text=Definition%20and%20Usage,iterator%20are%20paired%20together%20etc.

#---------------------------------------------------------------------------------------
# num = [1, 2, 3, 4]
# letters = ['a', 'b', 'c', 'd', 'e']
# zipped = zip(num, letters) # zip() function combines the two lists into a single list of tuples. In this example, the resulting list will have a length of 4, as it is the length of the shortest input list. The excess elements in the longer list are ignored. We can display a readable output by converting the zipped object to a list.
# print(list(zipped)) # [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
#---------------------------------------------------------------------------------------

# list students who have grades below 80

zip_list = zip(students, grades, activities)


for student, grade, activity in zip_list:
    if grade < 80:
       print(student, grade, activity)



#---------------------------------------------------------------------------------------
# list students who have grades above 80

students_approved = []
zip_list2 = zip(students, grades)

for student, grade in zip_list2:
    if grade > 80:
        students_approved.append(student)
        
print("Students approved = ", students_approved)

