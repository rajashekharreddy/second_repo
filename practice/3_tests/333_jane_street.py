"""
Given integers M and N, write a program that counts how many positive integer pairs (a, b) satisfy the following conditions:

a + b = M
a XOR b = N

"""


def num_pairs(m,n):

	count = 0

	for a in range(m):
		b = m - a
		#print(a,b, a^b)

		if a ^ b == n:
			print("Here is {}^{} == {}".format(a,b,n))
			count += 1

	return count

print(num_pairs(73,41))
