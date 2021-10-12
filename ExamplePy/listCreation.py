
students = []
for i in range(3):
	student = {}
	nameInput = input("Enter student " + str(i) + " name: ")
	student["name"] = nameInput
	courseInput = input("Enter student " + str(i) + " course: ")
	student["course"] = courseInput
	graduationInput = int(input("Enter student " + str(i) + " year of graduation: "))
	student["year"] = graduationInput
	students.append(student)
print(students)

