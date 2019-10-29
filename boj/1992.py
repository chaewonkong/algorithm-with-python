"""쿼드트리

ID: 1992
URL: https://www.acmicpc.net/problem/1992

흑백 영상을 압축하여 표현하는 데이터 구조로 쿼드 트리(Quad Tree)라는 방법이 있다.
흰 점을 나타내는 0과 검은 점을 나타내는 1로만 이루어진 영상(2차원 배열)에서
같은 숫자의 점들이 한 곳에 많이 몰려있으면, 
쿼드 트리에서는 이를 압축하여 간단히 표현할 수 있다.

주어진 영상이 모두 0으로만 되어 있으면 압축 결과는 "0"이 되고, 
모두 1로만 되어 있으면 압축 결과는 "1"이 된다. 
만약 0과 1이 섞여 있으면 전체를 한 번에 나타내지를 못하고, 
왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래, 
이렇게 4개의 영상으로 나누어 압축하게 되며, 
이 4개의 영역을 압축한 결과를 차례대로 괄호 안에 묶어서 표현한다.
N ×N 크기의 영상이 주어질 때, 
이 영상을 압축한 결과를 출력하는 프로그램을 작성하시오.

[입력]
첫째 줄에는 영상의 크기를 나타내는 숫자 N 이 주어진다. 
N 은 언제나 2의 제곱수로 주어지며, 1≤N ≤64의 범위를 가진다. 
두 번째 줄부터는 길이 N 의 문자열이 N 개 들어온다. 
각 문자열은 0 또는 1의 숫자로 이루어져 있으며, 영상의 각 점들을 나타낸다.

[출력]
영상을 압축한 결과를 출력한다.

[예제 입력]
8
11110000
11110000
00011100
00011100
11110000
11110000
11110011
11110011

[예제 출력]
((110(0101))(0010)1(0001))
"""

def compress(matrix):
    ret = ""

    def is_all_same(r, c, size, color):
        for dr in range(size):
            for dc in range(size):
                if matrix[r+dr][c+dc] != color:
                    return False
        return True
    
    def generate(r, c, size):
        nonlocal ret
        color = matrix[r][c]

        if size == 1 or is_all_same(r, c, size, color):
            ret += str(color)
        else:
            ret += "("
            size //= 2
            for i in range(2):
                for j in range(2):
                    generate(r + size *i, c + size * j, size)
            ret += ")"
    
    generate(0, 0, len(matrix))

    return ret


if __name__ == "__main__":
    N = int(input())
    matrix = [[int(l) for l in input()] for _ in range(N)]
    print(compress(matrix))