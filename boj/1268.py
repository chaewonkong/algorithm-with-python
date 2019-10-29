"""임시 반장 정하기

6학년 1반 담임을 맡게 되었다. 
선생님은 우선 임시로 반장을 정하고 학생들이 서로 친숙해진 후에 
정식으로 선거를 통해 반장을 선출하려고 한다. 
그는 자기반 학생 중에서 1학년부터 5학년까지 지내오면서 
한번이라도 같은 반이었던 사람이 가장 많은 학생을 임시 반장으로 정하려 한다.

각 학생들이 1학년부터 5학년까지 속했던 반이 주어질 때, 임시 반장을 정하는 프로그램을 작성하시오.

[예제 입력]
5
2 3 1 7 3
4 1 9 6 8
5 5 2 4 4
6 5 2 6 7
8 4 2 2 2

[예제 출력]
4
"""
def decide_president(board):
    CLASS = 5
    N = len(board)
    ans = [0] * (N)
    g = [[0] * N for _ in range(N)]
    
    def is_connected(a, b):
        return g[a][b]
    
    def connect(a, b):
        g[a][b] = 1
        g[b][a] = 1
        
    for c in range(CLASS):
        one_year = [(board[i][c], i) for i in range(N)]
        one_year.sort()
        tmp = [one_year[0]]

        for tup in one_year[1:]:
            # tup := one item in one_year list
            # tup[0]: class
            # tup[1]: student
            if tup[0] == tmp[-1][0]:
                for cls, student in tmp:
                    if not is_connected(student, tup[1]):
                        ans[student] += 1
                        ans[tup[1]] += 1
                        connect(student, tup[1])
                tmp.append(tup)
            else:
                tmp = [tup]
    
    return min(i+1 for i in range(N) if ans[i] == max(ans))

if __name__ == '__main__':
    N = int(input())
    board = []
    for _ in range(N):
        board.append([int(n) for n in input().split()])
        
    print(decide_president(board))