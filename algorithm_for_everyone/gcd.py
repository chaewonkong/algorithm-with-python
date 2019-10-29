"""Greatest Common Devisor in Python

return greatest common devisor about input int a and int b"""


def gcd(a, b):
	"""Return greatest common devisor of int a, b"""

	common_dev = []

	for n in range(1, min(a,b)+1):
		if a % n == 0 and b % n ==0:
			common_dev.append(n)

	return max(common_dev)