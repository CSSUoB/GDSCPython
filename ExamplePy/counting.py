target = int(input("Enter target value: "))
if target <= 10 and target > 0:
	print("I can count to that!")
	for x in range(target + 1):
		print(x)
elif target < 0:
	print("I don't have negative fingers!")
else:
	print("That number is too high!")
