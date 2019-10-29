"""Names Scores, from Project Euler No.22

Using names.txt, a 46K text file containing over five-thousand first names, 
begin by sorting it into alphabetical order. 
Then working out the alphabetical value for each name, 
multiply this value by its alphabetical position 
in the list to obtain a name score.

Return total of all the name scores in the file."""
import requests
from bs4 import BeautifulSoup


def alphabet_score(name):
	"""Return sum of each alphabet's score for given name"""

	score = 0
	for i in name:
		if i == '"':
			pass
		else:
			score += (ord(i) - ord('A') + 1)

	return score


def names_score():
	"""Return sum of all names' scores for given name file"""

	req = requests.get('http://euler.synap.co.kr/files/names.txt')
	html = req.text
	soup = BeautifulSoup(html, 'html.parser')
	
	f = soup.text
	names = f.split(',')

	names.sort()

	for i in range(len(names)):
		names[i] = (i+1) * alphabet_score(names[i])

	return sum(names)

print(names_score())

