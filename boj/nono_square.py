"""제곱ㄴㄴ수"""

range_input = input()
range_list = range_input.split(' ')
minimum = int(range_list[0])
maximum = int(range_list[1])


def nono_square(minimum, maximum):

	n = len(range(minimum, maximum+1))
	for x in range(minimum, maximum+1):
		if x > 3:
			root_x = int(x ** 0.5)

			for k in range(2, root_x+1):
				if is_prime(k):
					if x % (k**2) ==0:
						n -=1
						break

	return n


import math
def is_prime(number):
	if number ==2:
		return True
	else:
		for x in range(2, int(math.sqrt(number))+1):
			if number % x ==0:
				return False
				break
	return True



print(nono_square(minimum, maximum))

