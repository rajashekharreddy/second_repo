"""
Input: arr[] = {3, 1, 4, 6, 5}
Output: True
There is a Pythagorean triplet (3, 4, 5).

Input: arr[] = {10, 4, 6, 12, 5}
Output: False
There is no Pythagorean triplet.


Given an array of integers, write a function that returns true if there is a triplet (a, b, c) that satisfies a2 + b2 = c2.
"""

def pythogeran(array):

	for i in range(len(array)-2):

		for j in range(i+1, len(array)-1):

			for k in range(j+1, len(array)):

				print(array[i]**2, array[j]**2, array[k]**2)

				if (array[i]**2 == array[j]**2 + array[k]**2) or (array[j]**2 == array[i]**2 + array[k]**2) \
					or (array[k]**2 == array[i]**2 + array[j]**2) :

					return array[i], array[j], array[k]

	return False


print(pythogeran([3, 1, 4, 6, 5]))