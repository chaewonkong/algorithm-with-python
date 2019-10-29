"""Baekjoon Online Judge No.1157

Most Frequent Alphabet in Python

[Input]
Input is a tring of alphabets shorter than 1,000,000.
Alphabets could be lowercase, uppercase or mixed.

[Output]
Print most frequently used alphabet in uppercase.
If there is more than one alphabet, print '?' instead.
"""


def most_frequent_alphabet(string):
	"""For given string s return most frequent alphabet in uppercase.

	If the number of the most frequent alphabet is more than 1,
	return '?' Instead"""

	string = string.lower()
	dic = {}
	letters = []
	count = 0

	for s in string:
		if s in dic:
			dic[s] += 1
		else:
			dic[s] = 1

	for item in dic:
		if dic[item] > count:
			count = dic[item]
			letters = [item]
		elif dic[item] == count:
			letters.append(item)

	if len(letters) == 1:
		return letters[0].upper()
	else:
		return '?'


if __name__ == "__main__":
	string = input()
	print(most_frequent_alphabet(string))

