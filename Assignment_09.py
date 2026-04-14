# Create a Dictionary of Student Marks
#Create a dictionary where student names are keys and their marks are values.
student_marks = {
    "Jaya  ": 85,
    "Ravi": 72,
    "Rohan": 90,
    "Dev": 65
}
student_name = input("Enter the student's name: ").strip().title()
marks = student_marks.get(student_name)

if marks is not None:
    print(f"The marks for {student_name} are: {marks}")
else:
    print(f"Error: Student '{student_name}' not found in the dictionary.")