input1 = "test1."
input2 = "test2'"
illegalChars = ".',"
for char in list(illegalChars):
	print(char)
	input1 = input1.replace(char, "")
	print("!!" + input1)
	input2 = input2.replace(char, "")