""" BaekJoon Online Judge No.1065

어떤 양의 정수 n에 대해 n의 각 자리수가 등차수열을 이루면 n은 '한수'라고 한다.
1000 이하의 N이 주어질  때, 1 <= X 이고, X <= N인 X의 개수를 출력하라
"""


def hansu(limit):
	""" 1 이상 limit 이하의 한수의 개수를 출력하라
	(limit <= 1000)"""

	count = 0

	for n in range(1, limit+1):
		# 자리수가 2개 이하이면 무조건 등차수열
		if n < 100:
			count +=1
		elif n < 1000:
			first = n//100
			second = (n//10) % 10
			third = n % 10

			if (first + third)/2 == float(second):
				count +=1
	return count


if __name__ == '__main__':
	limit = int(input())
	print(hansu(limit))
