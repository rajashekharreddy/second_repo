import io, time

with io.open("log2.txt", "r") as file_obj:

	new_dict = dict()

	while True:

		line = file_obj.readline()

		if line.strip() in new_dict:

			new_dict[line.strip()] += 1

		else:

			new_dict[line.strip()] = 1

		time.sleep(0.1)

		print(new_dict)

