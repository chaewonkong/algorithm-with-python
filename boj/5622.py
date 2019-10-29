"""Baekjoon Online Judge No.5622

다이얼"""


def runtime(string):
	runtime = {
				3: ['A', 'B', 'C'], 
				4: ['D', 'E', 'F'],
				5: ['G', 'H', 'I'],
				6: ['J', 'K', 'L'],
				7: ['M', 'N', 'O'],
				8: ['P', 'Q', 'R', 'S'],
				9: ['T', 'U', 'V'],
				10: ['W', 'X', 'Y', 'Z']
				}
	total = 0

	for letter in string:
		for i in range(3, 11):
			if letter in runtime[i]:
				total += i

	return total


if __name__ =="__main__":
	string = input()
	print(runtime(string))