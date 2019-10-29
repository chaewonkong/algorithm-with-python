"""Sieve of Eratosthenes

Baekjoon Online Judge No.1929

two number m, n (m < n) are given as input in the first line, 
separated by whitespace.
Print all prime numbers between m, n line by line.
"""

def sieve(start, end):
	"""Return list of prime numbers between start, end"""

	arr = [n for n in range(2, end+1)]
	arr = [0, 0] + arr

	for i in range(2, end+1):
		j = 2
		while i * j <= end:
			arr[i*j] = 0
			j += 1
	
	for l in arr:
		if l != 0 and start <= l and l <= end:
			print(l)
	

if __name__ == "__main__":
	m, n = map(int, input().split(" "))
	
	sieve(m, n)

