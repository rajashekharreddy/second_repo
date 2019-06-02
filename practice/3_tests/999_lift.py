
def exclude_nums(nums):
	output = list()
	for i in range(len(nums)):
		product = 1
		for j in range(len(nums)):

			if i != j:

				product *= nums[j]

		output.append(product)
	return output


print(exclude_nums([2,3,4,5,6]))