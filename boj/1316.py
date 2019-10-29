"""Baekjoon Online Judge No.1316

Group Words Checker in Python

Group word is a word that for every character in the word, each type of caracter only appears continuously.

ex. 'ccaaabb' is a group word, whereas 'ccaabba' is not,
for 'ccaabba', 'a' appears continuously two times and after two more 'b's, 
it appears again.

ex. 'kin' is also a group word, since each character appears continuously, eventhough it appears only once.

[INPUT]
number of words N is given in the first line.
N number words are given from second line.
Each word is consist of alphabetic lowercase and max length below 100.
There is no two identical words.

[OUTPUT]
Print number of 'group words' in the first line.
"""

def is_group_word(word):
	"""Return True if word is group word or return False"""

	letters = [letter for letter in word]
	index = {}

	for i in range(len(letters)):
		if word[i] in index:
			if index[word[i]] == i-1:
				index[word[i]] += 1
			else:
				return False
				break
		else:
			index[word[i]] = i

	return True


# Run block
if __name__ == "__main__":
	rounds = int(input())
	group_words = []

	for _ in range(rounds):
		word = input()
		if is_group_word(word):
			group_words.append(word)

	print(len(group_words))



