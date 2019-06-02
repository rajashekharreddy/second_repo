

def count_letters(str1):

	upper = 0
	lower = 0

	for letter in str1:

		if not isinstance(letter, int):

			if letter.isupper():

				upper += 1

			else:

				lower += 1

	return upper,lower

print(count_letters("abcDEFc"))




dict = {"x":10, "y":20, "c":30}
dict2= {"b":15}

for key, value in dict.items():

	print(key,value)


dict.update(dict2)
print(dict)



#m2_start: 2.75c

import re

#re.match()

#r"[m2_start.*"




class student(A,B,C):

	def __init__(self, st1,st2,st3):

		self.st1 = st1
		self.st2 = st2
		self.st3 = st3

	def adding(self):

		return (self.st1 + self.st2 + self.st3)/3.0


inst1 = student(25,25,55)

print(inst1.adding())






