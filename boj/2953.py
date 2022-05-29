# https://www.acmicpc.net/problem/2953

def calc_score(scores):
    total = 0
    for s in scores:
        total += int(s)
    
    return total


if __name__ == "__main__":
    max_score = 0
    idx = -1
    for i in range(5):
        s = input()
        arr = s.split(" ")
        score = calc_score(arr)
        max_score = max(max_score, score)
        if max_score == score:
            idx = i
    
    print(idx+1, max_score)

