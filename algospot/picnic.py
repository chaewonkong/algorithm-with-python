"""소풍 (난이도: 하)

ID: PICNIC
URL: https://algospot.com/judge/problem/read/PICNIC

안드로메다 유치원 익스프레스반에서는 다음 주에 율동공원으로 소풍을 갑니다. 
원석 선생님은 소풍 때 학생들을 두 명씩 짝을 지어 행동하게 하려고 합니다. 
그런데 서로 친구가 아닌 학생들끼리 짝을 지어 주면 서로 싸우거나 같이 돌아다니지 않기 때문에, 
항상 서로 친구인 학생들끼리만 짝을 지어 줘야 합니다.

각 학생들의 쌍에 대해 이들이 서로 친구인지 여부가 주어질 때, 
학생들을 짝지어줄 수 있는 방법의 수를 계산하는 프로그램을 작성하세요. 
짝이 되는 학생들이 일부만 다르더라도 다른 방법이라고 봅니다. 
예를 들어 다음 두 가지 방법은 서로 다른 방법입니다.

(태연,제시카) (써니,티파니) (효연,유리)
(태연,제시카) (써니,유리) (효연,티파니)


[입력]
입력의 첫 줄에는 테스트 케이스의 수 C (C <= 50) 가 주어집니다. 
각 테스트 케이스의 첫 줄에는 학생의 수 n (2 <= n <= 10) 과 
친구 쌍의 수 m (0 <= m <= n*(n-1)/2) 이 주어집니다. 
그 다음 줄에 m 개의 정수 쌍으로 서로 친구인 두 학생의 번호가 주어집니다. 
번호는 모두 0 부터 n-1 사이의 정수이고, 같은 쌍은 입력에 두 번 주어지지 않습니다. 
학생들의 수는 짝수입니다.

[출력]
각 테스트 케이스마다 한 줄에 모든 학생을 친구끼리만 짝지어줄 수 있는 방법의 수를 출력합니다.

[예제 입력]
3 
2 1 
0 1 
4 6 
0 1 1 2 2 3 3 0 0 2 1 3 
6 10 
0 1 0 2 1 2 1 3 1 4 2 3 2 4 3 4 3 5 4 5

[예제 출력]
1
3
4
"""
 
''' 성환 답
def get_ways(are_frieds):
    N = len(are_frieds)
    taken = [0]*N

    def find(left):
        if left == 0:
            return 1
        for i in range(N):
            if not taken[i]:
                nxt = i
                break
        ans = 0
        for i in range(nxt+1, N):
            if not taken[i] and are_frieds[nxt][i]:
                taken[i] = taken[nxt] =1
                ans += find(left-2)
                taken[i] = taken[nxt] = 0
        return ans
    return find(N)
'''

def get_options(are_friends):
    N = len(are_friends)
    taken = [0] * N

    def find(left):
        count = 0
        if left == 0:
            return 1
        for i in range(N):
            if not taken[i]:
                nxt = i
                break
        for j in range(nxt+1, N):
            if not taken[j] and are_friends[nxt][j]:
                taken[j] = taken[nxt] = 1
                count += find(left-2)
                taken[j] = taken[nxt] = 0
        return count
    
    return find(N)



if __name__ == "__main__":
    # Three Example Test Cases
    T = int(input())
    results = []
    for _ in range(T):
        n, m = [int(i) for i in input().split()]
        temp = [int(i) for i in input().split()]
        are_friends = [[0]*(n) for _ in range(n)]
        idx = 0
        while idx < len(temp):
            are_friends[temp[idx]][temp[idx+1]] = are_friends[temp[idx+1]][temp[idx]] = 1
            idx += 2
        results.append(get_options(are_friends))
    
    for ret in results:
        print(ret)
            

