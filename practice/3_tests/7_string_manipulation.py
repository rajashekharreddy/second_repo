#"abcieaveiasd"
# if "c" infront then "cei"
# if "ie" are adjacent "ie"


def string_manipulation(input1):

	output = ""
	i = 0
	while i <= (len(input1)-1):

		if input1[i] == "c":

			if input1[i+1:i+3] == "ie" or input1[i+1:i+3] == "ei":

				output += "cei"
				i += 3

			else:

				output += input1[i]
				i += 1

		elif input1[i] == "i" or input1[i] == "e":

			if input1[i+1:i+2] == "i" or input1[i+1:i+2] == "e":

				output += "ie"
				i += 2

			else:

				output += input1[i]
				i += 1

		else:

			output += input1[i]
			i += 1
	return output

print(string_manipulation("abcieaveiasd"))