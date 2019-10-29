"""Morse Code Dictionary

Problem from Algospot

ID: MORSE
URL: https://algospot.com/judge/problem/read/MORSE

n개의 장점과 m개의 단점으로 구성된 모든 신호들을 담고 있는 사전이 있다고 합시다. 
예를 들어 n = m = 2라면 다음과 같은 신호들이 포함되어 있는 것이죠.
    --oo
    -o-o
    -oo-
    o--o
    o-o-
    oo--

이 신호들은 사전순서대로 정렬되어 있습니다. -의 아스키 코드는 45이고, 
o의 아스키 코드는 111이기 때문에 -가 먼저 오게 되죠. 
n과 m이 주어질 때 이 사전의 k번째 신호를 출력하는 프로그램을 작성해 봅시다. 
예를 들어 위 사전에서 네 번째 신호는 o--o입니다

[입력]
입력의 첫 줄에는 테스트 케이스의 수 C(≤50)가 주어집니다. 
각 테스트 케이스는 세 개의 정수 n, m(1≤n, m≤100), 
k(1≤k≤1,000,000,000)로 주어집니다. 
사전에는 항상 k개 이상의 신호가 있다고 가정해도 좋습니다.

[출력]
각 테스트 케이스마다 한 줄에 해당 신호를 출력합니다.

[예제입력]
3
2 2 4
4 8 13
6 4 1

[예제출력]
o--o
--o-ooo-oooo
------oooo
"""

long = '-'
short = 'o'

def k_th_morse(n, m, k):
    """Return k th morse code in dictionary,
    consist of n number of '-' and m number of 'o'"""





if __name__ == "__main__":
    NUM_OF_CASES = int(input())
    for i in range(NUM_OF_CASES):
        case = input().split(" ")
        n, m, k = case
        n, m, k = int(n), int(m), int(k)
        print(k_th_morse(n, m, k))
