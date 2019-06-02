#Integer to Roman
#  I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1,000

int_roman = {1:"I", 4:"IV", 5:"V", 9:"IX", 10:'X', 40:"XL", 50:"L", 90:"XC", 100:"C", 400:"CD", 500:"D", 900:"CM", 1000:"M"}

def roman(num):

	nums = list()
	length = len(str(num)) - 1
	for element in str(num):

		nums.append(int(element) * (10 ** length))
		length -= 1

	#print(nums)
	output = ""
	for element in nums:

		if element in int_roman.keys():

			output = output + int_roman[element]

		else:

			if len(str(element)) == 4 and element :

				output = output + (int(str(element)[0:1]) * int_roman[1000])

			elif len(str(element)) == 3 and element < 400 :

				output = output + (int(str(element)[0:1]) * int_roman[100])

			elif len(str(element)) == 3 and element > 500 :

				output = output + int_roman[500] + ((int(str(element)[0:1]) - 500)*int_roman[100])

			elif len(str(element)) == 2 and element < 40 :

				output = output + (int(str(element)[0:1]) * int_roman[10])

			elif len(str(element)) == 2 and element > 50 :

				output = output + int_roman[50] + ((int(str(element)[0:1]) - 50)*int_roman[10])

			elif len(str(element)) == 1 and element < 4 :

				output = output + (int(str(element)[0:1]) * int_roman[1])

			elif len(str(element)) == 1 and element > 5 :

				output = output + int_roman[5] + ((int(str(element)[0:1]) -5) * int_roman[1])

	return nums, output




for i in range(213, 313):

	print(roman(i))