"""Same Name Finder

Find same name(s) in given list and return them as a set"""


def find_same_name(names):
	"""From given list of names, return all names that are overlapped"""

	results = set()
	while names:
		name = names.pop(0)
		if name in names:
			results.add(name)

	return results


if __name__ == "__main__":
	names = ['Tom', 'Harry', 'Tom', 'Jake', 'Jake', 'Hal', 'Leon', 'Peter', 'Leon', 'Leon']

	for name in find_same_name(names):
		print(name)
