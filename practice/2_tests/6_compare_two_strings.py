
def compare_two_strings(s1, s2):
	
	if len(s1) != len(s2):
		return False

	else:

		for i in range(len(s1)):

			if s1[i].lower() != s2[i].lower():

				return False
		return True

print(compare_two_strings("abcDV", "AbCdv"))