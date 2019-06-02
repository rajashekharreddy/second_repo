"""
Given a string, find the length of the smallest window that contains every distinct character. 
Characters may appear more than once in the window.

For example, given "jiujitsu", you should return 5, corresponding to the final five letters.

"""

def distinct(given):

	all_distinct = set(given)
	smallest = 0
	for i in range(len(given)-1):

		for j in range(i+1, len(given)):

			if set(given[i:j+1]) == all_distinct:

				if smallest == 0:

					smallest = len(given[i:j+1])

				if smallest > len(given[i:j+1]):

					smallest = len(given[i:j+1])
	return smallest





print(distinct("jiujitsu"))