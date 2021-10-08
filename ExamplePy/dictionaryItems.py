person = {
	"name" : "Bob",
	"phoneNumber" : "12345-123456"
}
targetPerson = input("I want to contact: ")
if person["name"] == targetPerson:
	print(person.get("phoneNumber"))
else:
	print("No contact info")
