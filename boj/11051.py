"""Binominal Coefficient Algorithm 

from Baekjun Online Judge no.11051

For given natural number n and integer k, 
return the result value of n combination k (nCk) divided by 10,007
"""


n, k = map(int, input().split(' '))

def dynamic_c(n, k):
	"""Return n combination c divided by 10007, using dynamic programming"""

	dt = [[0 for _ in range(k+1)] for _ in range(n+1)]

	for i in range(n+1):
		for j in range(min(i, k)+1):
			if i==j or j==0:
				dt[i][j] = 1
			else:
				dt[i][j] += dt[i-1][j] + dt[i-1][j-1]

	return dt[n][j] % 10007

print(dynamic_c(n, k))