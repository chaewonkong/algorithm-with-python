"""Project Euler No.16

Power Digit Sum in Python

215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
Return sum of the digits of the number 2^1000."""


def power_digit_sum(power):
	"""Return sum of the digits of 2**power"""

	int_val = 2 ** power
	str_val = str(int_val)
	total = 0

	for i in range(len(str_val)):
		total += int(str_val[i])

	return total


if __name__ == "__main__":
	print(power_digit_sum(1000))
