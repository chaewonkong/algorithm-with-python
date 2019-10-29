"""BaekJoon Online Judge No.10039

Finding Average of Array with Condition
in Python

For given five int inputs of multiple of 5, 
if input is less than 40, change to 40,
Return average of adjusted array."""

if __name__ == "__main__":
	score = []
	for _ in range(5):
		score.append(int(input()))

	for i in range(5):
		if score[i] < 40:
			score[i] = 40

	print(sum(score)//5)