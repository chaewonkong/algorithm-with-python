"""GCD/LCM Calculator in Python

from BaekJoon Online Judge No.2609

Return greatest common divisor and least common multiple
for given two natural numbers"""


def gcd_lcm(n1, n2):
	"""Return GCD and LCM"""
	a, b = n1, n2
	while b:
		a, b = b, a%b
	gcd = a

	lcm = (n1*n2)//gcd

	return gcd, lcm


if __name__ == '__main__':
	a, b = map(int, input().split(' '))
	
	for result in gcd_lcm(a, b):
		print(result)