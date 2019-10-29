"""Linear Search Example in Python

Return student name from given student number, by using linear search."""


def search_name(number, stu_no, stu_name):
	"""Return student's name by given number"""

	stu_dic = {}
	for i in range(len((stu_no))):
		stu_dic.update({stu_no[i]: stu_name[i]})

	if number in stu_dic.keys():
		return stu_dic[number]
	else:
		return '?'


def search_name_linear(number, stu_no, stu_name):
	"""Search student name by number using linear search"""

	for i in range(len(stu_no)):
		if stu_no[i] == number:
			return stu_name[i]

	return '?'