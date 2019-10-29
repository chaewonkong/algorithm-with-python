# Combinations

def get_all_combinations(arr, N):
    """Return all combinations of N number item from given arr"""
    combinations = []
    picked = []
    used = [0] * len(arr)

    def find(picked, topick):
        """get combinations by recursion"""
        if topick == 0:
            ret = [arr[i] for i in picked]
            # used라는 리스트를 만들고 거기에 사용 여부를 담으면 O(1)로 접근 가능하다
            combinations.append(ret)
            return
        start = picked[-1] + 1 if picked else 0
        for i in range(start, len(arr)):
            if i == 0 or arr[i] != arr[i-1] or used[i-1]:
                picked.append(i)
                used[i] = 1
                find(picked, topick-1)
                picked.pop()
                used[i] = 0
    
    find(picked, N)
    return combinations

if __name__ == "__main__":
    # Get list of elements divided by whitespace in the first line
    # Get number of items to pick in the second line
    print(get_all_combinations([elm for elm in input().split()], int(input())))