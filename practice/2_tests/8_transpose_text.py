

with open("example.txt", "r") as file_obj:
	data = list()
	for line in file_obj:

		data.append(line.strip().split(" "))
	print(data)

with open("ouput.txt", "w") as file_obj:
	for j in range(len(data[0])):
		line = ""
		for i in range(len(data)):

			line = line + " " + data[i][j]
		print(line)
		file_obj.write(line)
		file_obj.write("\n")