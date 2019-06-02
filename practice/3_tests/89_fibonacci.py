#fib = [0,1,1,2,3,5,8,13,21]
"""
def fib_nums(num):

	if num == 1:
		return 0

	elif num == 2:
		return 1

	else:

		return fib_nums(num-1) + fib_nums(num-2)
"""

def fib_nums(num):

	fibs = [0,1]

	for i in range(2, num):

		fibs.append(fibs[-1] + fibs[-2])

	return fibs[num-1]


print(fib_nums(350))