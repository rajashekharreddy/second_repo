from itertools import permutations
given = "HACK 2"
word, num = given.split(" ")[0], int(given.split(" ")[1])
print(word, num)

output = list(permutations(sorted(word),num))
print(output)
for i in output:
    print("".join(i))