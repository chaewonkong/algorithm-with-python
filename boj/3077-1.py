def get_score(answers, submitted):
    N = len(answers)
    total_pairs = int(N/2*(N-1))
    ans = 0
    tmp_arr = [0] * N
    
    for i in range(N):
        target = answers[i]
        tmp_arr[i] = submitted.index(target)
    
    def find(chosen):
        nonlocal ans
        if len(chosen) == 2:
            a, b = chosen
            ans += (tmp_arr[a] < tmp_arr[b])
            return
        start = chosen[-1] +1 if chosen else 0
        for nxt in range(start, N):
            chosen.append(nxt)
            find(chosen)
            chosen.pop()
    
    find([])
    return ans, total_pairs

if __name__ == "__main__":
    input()
    answers = [n for n in input().split()]
    submitted = [n for n in input().split()]
    n, total = get_score(answers, submitted)
    print(n, '/', total, sep="")