"""
문제 설명
입력받은 숫자를 우리가 읽는소리로 출력하는 코드를 작성하시오.

제약사항 
입력값은 1 ~ 99999의 정수에 한함.

입출력 예

input	answer
2001	"이천일"
98030	"구만팔천삼십"
11010	"만천십"
"""

PLACE = ["", "십", "백", "천", "만"]
DECIMAL = ["", "일", "이", "삼", "사", "오", "육", "칠", "팔", "구"]

def read(n):
    ret = ""
    length = len(str(n))
    d = 0
    while n > 0:
        if d == 0:
            ret = DECIMAL[n % 10] + ret
        else:
            if n % 10 == 1:
                ret = PLACE[d] + ret
            elif n % 10 == 0:
                ret = DECIMAL[n%10] + ret
            else:
                ret = DECIMAL[n%10] + PLACE[d] + ret
        n //= 10
        d += 1
    return ret


if __name__ == "__main__":
    N = int(input())
    print(read(N))