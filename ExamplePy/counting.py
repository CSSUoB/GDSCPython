target = int(input("Enter target value: "))
if target <= 10:
	print("I can count to that!")
	for x in range(target + 1):
		print(x)
else:
	print("That number is too high!")
