'''LSD Radix Sort

sort the given list of integers by sorting from least digit to most significant digit'''


def max_digit(values):
	'''Add '0' to elements to make them as same digit number'''

	int_max = max(values)
	digit_max = len(str(int_max))
	values = [str(v) for v in values]
	result = [] # Contain converted outcomes

	for v in values:
		required = digit_max - len(v)
		result.append(required * '0' + v)

	return result


def radix_sort(values):
	'''Sort given list by using radix sort starting from least significant digit.

	Only works for plus integers.'''

	values = max_digit(values)
	digit_max = len(values[0])
	temp = []
	result = []

	for units in range(1, digit_max +1):
		# Contain all the digits of same units into temp list
		for i in range(len(values)):
			if values[i][-units] not in temp:
				temp.append(values[i][-units])
			temp.sort()
		# print(temp)

		# Sort values list by comparing the units
		for t in temp:
			index = 0
			length = len(values)
			while index < length:
				# Contain value in result list as order
				if values[index][-units] == t:
					result.append(values.pop(index))
					length = len(values)
				else:
					index += 1
				
		# Reset all the lists for next sequence
		values = result
		temp = []
		result = []

	# Retern ordered values in integer form
	for i in values:
		result.append(int(i))

	return result

#List given
integers = [256, 56, 8, 2974, 13, 2972, 88] # List of integers given

print(radix_sort(integers))


