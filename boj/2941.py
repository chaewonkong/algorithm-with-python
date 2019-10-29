"""Baekjoon Online Judge No.2941

Croatian Alphabet Length Counter

In Early version of Operating Systems, Croatian alphabets were not available.
Therefore, People converted it to unique signs.

'c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=' are those converted version.
Other alphabets are the same as english alphabet.

Return number of Croatian alphabets in given string.

[INPUT]
String length less than equal to 100 is given as input.
The string only contains lowercase alphabet and '-', '='.

[OUTPUT]
Print number of Croatian alphabets in the string.
"""


def croatian_alphabet(string):
	"""Return number of Croatian letters in string"""

	croatian = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
	length = len(string)
	find_croatian = [[char, len(char), string.count(char)] for char in croatian]

	# Subtract over added lengths
	for i in range(len(find_croatian)):
		# "dz=" contains "z=", so add double subtracted value
		if find_croatian[i][0] == 'dz=':
			length += (string.count('dz=') * (len('z=') -1))
		
		overadded = find_croatian[i][1] - 1
		times = find_croatian[i][2]
		length -= overadded * times

	return length


if __name__ == "__main__":
	string = input()
	print(croatian_alphabet(string))