"""Baekjoon Online Judge No.2908

Maximum Backward Number, in Python

For given two number, compare backward-read numbers and return bigger one.

[INPUT]
Unidentical two three-digit numbers are given divided by whitespace. 
Both numbers are consist of only 1 to 9 numbers. (No 0)

[OUTPUT]
Return bigger number when both numbers are read backwardly."""


def backward_max(a, b):
	"""Compare backward version of three-digit number a, b 
	and return bigger one"""

	backward_a = (a%10) * 100 + ((a//10)%10) * 10 + a//100
	backward_b = (b%10) * 100 + ((b//10)%10) * 10 + b//100

	return max(backward_a, backward_b)


if __name__ == "__main__":
	a, b = map(int, input().split())
	print(backward_max(a, b))

