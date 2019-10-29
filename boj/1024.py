"""Sum of Sequence in Python

from BaekJoon Online Judge No.1024

Return Sequence of continuous natural number,
sum of which is N and length is at least L.
"""

'''
def sum_sequence(target, length):
	"""Return sequence, sum of which is target and length is above length"""

	while length <= 100:
		sequence = [i for i in range(1, length+1)]
		s = sum(sequence)

		while sequence[0] <= (target//length)+1:
			if s == target:
				return sequence
			else:
				sequence = [k+1 for k in sequence]
				s = sum(sequence)
		length +=1

	return -1
'''


def sum_sequence(target, length):
	start = 1

	


# Test Block
if __name__ == '__main__':
	target, length = map(int, input().split(' '))
	result = sum_sequence(target, length)

	if result == -1:
		print(-1)
	else:
		for num in sum_sequence(target, length):
			print(num, end=' ')

