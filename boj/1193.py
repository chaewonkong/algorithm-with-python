"""Finding Fractions, 

Baekjoon Online Judge no.1193

Find rule and return x th result"""


def fraction(n):
	"""Return nth fraction number"""

	k = 1
	arr = []

	while (k*(k+1)//2) < n:
		k += 1

	for j in range(1, k+1):
		l = k - j + 1
		if k % 2 == 0:
			arr.append(str(j) + '/' + str(l))
		else:
			arr.append(str(l) + '/' + str(j))

	before = (k*(k-1)//2)

	return arr[n-before-1]



if __name__ == "__main__":
	n = int(input())
	print(fraction(n))