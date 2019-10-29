"""Project Euler No.19

Counting Sundays 1st of the Month

1 Jan 1st, 1900 was Monday.
A leap year occurs on any year evenly divisible by 4, 
but not on a century unless it is divisible by 400.

Return number of Sundays on the first of the month during twentieth century.
"""


def is_leapyear(year):
	"""Return boolean results for leap year"""

	if year % 400 == 0:
		return True
	elif year % 4 == 0 and year % 100 != 0:
		return True
	else:
		return False


def what_day(date):
	"""Return whatday of given date"""

	day = ["mon", "tue", "wed", "thur", "fri", "sat", "sun"]
	year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	year_leap = [(i+1) if i is 28 else i for i in year]
	start = [1900, 1, 1]
	index = 0
	days = 0

	while start[0] < date[0] - 1:
		start[0] += 1
		if is_leapyear(start[0]):
			days += 366
		else:
			days += 365
	start[0] += 1
	for i in range(date[1] - (start[1])):
		if is_leapyear(start[0]):
			days += year_leap[i]
		else:
			days += year[i]

	days += date[2]
	index = days % 7

	if date[0] == 1900:
		return day[index -1]
	else:
		return day[index]


def count_sunday(start, end):
	""" Return the number of Sundays between start and end"""

	count = 0

	for year in range(start[0], end[0] +1):
		for month in range(1, 13):
			if what_day([year, month, 1]) == "sun":
				print([year, month, 1])
				count += 1

	return count


if __name__ == "__main__":
	start = [1901, 1, 1]
	end = [2000, 12, 31]

	print(count_sunday(start, end))
