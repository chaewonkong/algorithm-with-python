"""Is Anagram, in Python

Return True/False if given two words are anagrams."""


def is_anagram(word1, word2):
	"""Return True if word1 is anagram of word2, or return False"""

	list1 = list(word1)
	list2 = list(word2)

	list1.sort()
	list2.sort()

	if list1 == list2:
		return True
	else:
		return False


if __name__ == '__main__':
	word1, word2 = input().split(' ')
	print(is_anagram(word1, word2))




