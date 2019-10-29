'''
문제 설명
화학식은 원소 기호와 원소 개수 조합으로 표현한다. (원래 숫자는 아랫 첨자로 표기하지만, 편의상 일반적인 숫자 표기로 대체한다.)

올바른 형식이 아닌 화학식을 입력받아, 올바른 형식으로 바꾸어 출력하는 프로그램을 작성하시오.

입력은 원소 기호들이 앞에 모여있고 뒤에 원소 개수들이 모여있는 형식이며, 세부 규칙은 아래와 같다.

원소 기호는 대문자 1개 또는 대문자 1개+소문자 1개이다.
원소 개수 N은 1 <= N <= 10 이다. N = 1일 경우 출력할 때 숫자를 생략한다.
잘못된 데이터 형식(원소와 원소 개수의 짝이 맞지 않는 경우)인 경우에 error라고 출력한다.
예
입력	출력	설명
HO21	H2O	O1에서 1 생략
CO12	CO2	
HSO214	H2SO4	
NaCl1	error	Cl 개수가 없음
'''
# 10인 경우 고려 안됨

s = input()
length = len(s)
e = []
n = []

for i in range(length):
    if s[i].isnumeric():
        n.append(s[i])
    elif s[i].isupper():
        if i+1 < length and s[i+1].islower():
            e.append(s[i:i+2])
        else:
            e.append(s[i])
if len(e) != len(n):
    print("error")

else:
    ret = ""
    for j in range(len(e)):
        ret += e[j]
        if n[j] != "1":
            ret += n[j]
    print(ret)
