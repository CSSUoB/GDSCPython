import sys

fileName = sys.argv[1]
with open(filename, "r") as myFile:
	print(myFile.read())
