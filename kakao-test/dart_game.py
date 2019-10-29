"""2. 다트 게임 in Python

카카오 신입 공채 코딩 테스트 문제
http://tech.kakao.com/2017/09/27/kakao-blind-recruitment-round-1/

1. 다트 게임은 총 3번의 기회로 구성된다.
2. 각 기회마다 얻을 수 있는 점수는 0점에서 10점까지이다.
3. 점수와 함께 Single(S), Double(D), Triple(T) 영역이 존재하고 
	각 영역 당첨 시 점수에서 1제곱, 2제곱, 3제곱 (점수^1 , 점수^2 , 점수^3 )으로 계산된다.
4. 옵션으로 스타상(*) , 아차상(#)이 존재하며 스타상(*) 당첨 시 해당 점수와 바로 전에 얻은 점수를 각 2배로 만든다. 
	아차상(#) 당첨 시 해당 점수는 마이너스된다.
5. 스타상(*)은 첫 번째 기회에서도 나올 수 있다. 이 경우 첫 번째 스타상(*)의 점수만 2배가 된다. (예제 4번 참고)
6. 스타상(*)의 효과는 다른 스타상(*)의 효과와 중첩될 수 있다. 이 경우 중첩된 스타상(*) 점수는 4배가 된다. (예제 4번 참고)
7. 스타상(*)의 효과는 아차상(#)의 효과와 중첩될 수 있다. 이 경우 중첩된 아차상(#)의 점수는 -2배가 된다. (예제 5번 참고)
8. Single(S), Double(D), Triple(T)은 점수마다 하나씩 존재한다.
9. 스타상(*), 아차상(#)은 점수마다 둘 중 하나만 존재할 수 있으며, 존재하지 않을 수도 있다.

0~10의 정수와 문자 S, D, T, *, #로 구성된 문자열이 입력될 시 총점수를 반환하는 함수를 작성하라.

* 입력 형식
“점수|보너스|[옵션]”으로 이루어진 문자열 3세트.
예) 1S2D*3T

점수는 0에서 10 사이의 정수이다.
보너스는 S, D, T 중 하나이다.
옵선은 *이나 # 중 하나이며, 없을 수도 있다.


* 출력 형식
3번의 기회에서 얻은 점수 합계에 해당하는 정수값을 출력한다.
예) 37
"""


def dart_score(string):
	"""Return total score in number"""

	rounds = []
	bonus = ['S', 'D', 'T']
	str_scores= [str(i) for i in range(10)]

	for pos in range(len(string)):
		if string[pos] in str_scores:
			# in case the score is 10
			if string[pos+1] and string[pos+1] in str_scores:
				rounds.append(int(string[pos]+string[pos+1]))
			else:
				rounds.append(int(string[pos]))
		elif string[pos] in bonus:
			rounds[-1] **= (bonus.index(string[pos]) +1)
		elif string[pos] =='#':
			rounds[-1] *= -1
		else:
			# string[pos] == '#'
			if len(rounds) >1: # for previus score, if exists
				rounds[-2] *= 2
				rounds[-1] *= 2
			elif len(rounds) ==1:
				rounds[-1] *= 2

	return sum(rounds)


# Test block: True for All correct algorithm False for any incorrect
if __name__ == "__main__":
	dart_games = [
				['1S2D*3T', 37], 
				['1D2S#10S', 9], 
				['1D2S0T', 3], 
				['1S*2T*3S', 23],
				['1D#2S*3S', 5],
				['1T2D3D#', -4],
				['1D2S3T*', 59]
				]
	for i in range(len(dart_games)):
		score = dart_score(dart_games[i][0])
		if score != dart_games[i][1]:
			valid = False
			break
		else:
			valid = True

	print(valid)

