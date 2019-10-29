'''Above Average Score Ratio

1. Get first input that indicates total number of case sets.
2. For the number of case sets, get input for each case.
3. First number indicates number of total score, and next numbers indicates specific score.
4. Round off or add more zero in order to make place value as thousandths.
5. Print above-average-student ratio for the each case.'''


def avg_above_ratio(students, scores):
	'''Return percentage of students who get above-average score'''

	average = sum(scores) / students
	count = 0

	for score in scores:
		if score > average:
			count += 1

	students = students
	ratio = round(count / students * 100, 3)

	return ratio


def make_thousandths(result):
	'''Make place value to be thousandths by adding additional 0'''
	temp = [str(j) for j in result]
	result = []

	for k in temp:
		start_pos = k.find('.')
		if len(k[start_pos+1:]):
			k += (3-len(k[start_pos+1:])) * '0'
		result.append(k)

	return result


# Get input and calculate ratio and save in result list
case = int(input())
result = []

for i in range(case):
	raw = input()
	raw = raw.split()
	students = int(raw.pop(0))

	scores = [int(i) for i in raw]
	result.append(avg_above_ratio(students, scores))


# print the elements in ratio list line by line
ratio = make_thousandths(result)
for l in ratio:
	print("{}%".format(l))