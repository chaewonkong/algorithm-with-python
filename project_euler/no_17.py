"""Number Letter Counts from Project Euler, no.17

If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 inclusive were written out in words, 
how many letters would be used?
"""


# Number below 20

word = [[
		'', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 
		'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 
		'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'
		],
		[
		'', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 
		'eighty', 'ninety'
		]
	]


def letter_count(value):
	"""Return English words for given number value"""

	str_val = str(value)
	result = ''

	if value == 1000:
		result = word[0][int(str_val[0])] + ' ' + 'thousand'
	else:
		if value >= 100:
			result = word[0][int(str_val[-3])] + ' ' + 'hundred'

			# 10의자리와 1의자리 중 적어도 하나는 0이 아닌 경우
			if int(str_val[1::]) > 0:
				result = result + ' and '

			str_val = str_val[1::] #str_val에서 100의 자리를 없애고 다음 과정 진행

		if str_val[-1] =='0': #1의자리가 0인 경우
			result = result + word[1][int(str_val[-2])]
		elif int(str_val) < 20:
			result = result + word[0][int(str_val)]
		else:
			result = result + word[1][int(str_val[-2])] + '-' \
					+ word[0][int(str_val[-1])]
	
	letter_count = len(result) - result.count('-') - result.count(' ')
	
	return letter_count


def sum_letter_count():
	"""Return sum of all english number's letter count"""

	result = 0
	for i in range(1, 1001):
		result += letter_count(i)

	return result


print(sum_letter_count())


