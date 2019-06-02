#{[]{()}}


class stack():

	def __init__(self):

		self.ex_stack = list()

	def push(self, item):

		self.ex_stack.append(item)

	def pop(self):

		self.ex_stack.pop()

	def peak(self):

		return self.ex_stack[-1]

	def length(self):

		return len(self.ex_stack)

	def print_items(self):

		print(self.ex_stack)



"""
inst1.push("[")
inst1.push("]")
inst1.push("{")
inst1.print_items()
inst1.pop()
inst1.print_items()
"""

def balanced(given_str):
	inst1 = stack()
	open_list = ["[","{","("] 
	close_list = ["]","}",")"]

	for i in given_str:

		if i in open_list:

			inst1.push(i)

		else:

			if inst1.peak() == open_list[close_list.index(i)] and inst1.length() > 0:

				inst1.pop()

			else:

				return False

	if inst1.length() == 0:

		return True


print(balanced("{[]{()}"))



