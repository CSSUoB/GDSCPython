people = {
	"name" : "Bob",
	"phoneNumber" : "12345-123456"
}
person = input("I want to contact: ")
if people["name"] == person:
	print(people.get("phoneNumber"))
else:
	print("No contact info")
