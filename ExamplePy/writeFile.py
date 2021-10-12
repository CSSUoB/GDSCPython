import sys
fileName = sys.argv[1]
with open(filename, "w") as myFile:
	myFile.write("Hello world!")
