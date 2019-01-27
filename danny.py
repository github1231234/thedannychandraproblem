def calc(nums_perm):
	resultA = (((nums_perm[0] * 10) + nums_perm[1]) * nums_perm[2])
	if (resultA == ((nums_perm[3] * 10) + nums_perm[4])):
		resultB = ( resultA + ((nums_perm[5] * 10) + nums_perm[6]))
		if (resultB == ((nums_perm[7] * 10) + nums_perm[8])):
			print("ANSWER")
			print(nums_perm)
			return True
		else:
			return False
	else:
		return False

nums = list(range(1,10))

import itertools
Permutations = itertools.permutations(nums)

# try each combination until we get the answer
for L in list(Permutations):
	print(L)
	if (calc(L) == True):
		break;



	



	



