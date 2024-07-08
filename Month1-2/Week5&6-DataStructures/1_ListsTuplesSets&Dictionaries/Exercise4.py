# Create a dictionary to store information about a student (name, age, grades).

# Create a dictionary with student information
student_info = {"name": "George", "age": 21, "grades": [85, 90, 78]}

# Add a new key-value pair for the student's major
student_info["major"] = "Computer Science"

# Remove the age key-value pair
del student_info["age"]

# Access and print the student's name and major
name = student_info["name"]
major = student_info["major"]
print(f"Name: {name}, Major: {major}")
# Output: Name: George, Major: Computer Science
