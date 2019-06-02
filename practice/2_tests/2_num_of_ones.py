"""Write an algorithm that finds the total number 
of set bits in all integers between 1 and N."""



def nums_ones(n):

	total = 0

	for i in range(1, n):

		count = bin(i)[2:].count("1")
		total = total + count

	return total

print(nums_ones(60))