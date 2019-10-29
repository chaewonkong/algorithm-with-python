"""Project Euler No.14

Longest Collatz Sequence in Python

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence 
(starting at 13 and finishing at 1) contains 10 terms. 
Although it has not been proved yet (Collatz Problem), 
it is thought that all starting numbers finish at 1.

Return starting number, under one million, produces the longest chain."""


def longest_collatz(limit):
	"""Return starting number generating longest chain 
	of hailstone sequence numbers"""

	n =1
	longest = 0
	length = 0

	for n in range(1, limit+1):
		seq = [n]
		while n > 1:
			if n % 2 == 0:
				n //= 2
				seq.append(n)
			else:
				n = 3*n + 1
				seq.append(n)
		if len(seq) > length:
			length = len(seq)
			longest = seq[0]

	return longest


if __name__ == '__main__':
	print(longest_collatz(1000000))
