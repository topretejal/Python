student_details={
    'Janet': 78,
    'Surbhi': 85,
    'Mohit':82,
    'Lekha':98,
    'Emily':76
}
name = input("Enter the student's name: ")
try:
    print(f"{name}'s marks:",student_details[name])
except Exception as err:
    print("Student not found.")