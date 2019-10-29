"""감소하는 수

음이 아닌 정수 X의 자릿수가 가장 큰 자릿수부터 작은 자릿수까지 감소한다면,
그 수를 감소하는 수라고 한다. 
예를 들어, 321과 950은 감소하는 수지만, 322와 958은 아니다. 
N번째 감소하는 수를 출력하는 프로그램을 작성하시오. 
0은 0번째 감소하는 수이고, 1은 1번째 감소하는 수이다. 
만약 N번째 감소하는 수가 없다면 -1을 출력한다.

[입력]
첫째 줄에 N이 주어진다. N은 1,000,000보다 작거나 같은 자연수 또는 0이다.

[출력]
첫째 줄에 N번째 감소하는 수를 출력한다.

[예제 입력]
18

[예제 출력]
42
"""

N = int(input())
if N > 1022:
    print(-1)
else:
    dec_num = []
    for i in range(1, 1024):
        num = 0
        for j in range(9, -1, -1):
            if i & (1 << j) != 0:
                num = 10 * num + j
        dec_num.append(num)
    dec_num.sort()
    print(dec_num[N])

    # 1 << j
    # j 번째 자리를 1로 킨다.


LIMIT = 2**10 - 1


# def find_dec_num(n):
#     dec_nums = []
#     pool = [i for i in range(10)]

#     def find(to_pick, picked):
#         if to_pick == 0:
#             ret = int("".join(str(pool[i]) for i in picked))
#             if ret not in dec_nums:
#                 dec_nums.append(ret)
#                 return
#         start = picked[-1]-1 if picked else 9
#         for i in range(start, -1, -1):
#             if i not in picked:
#                 picked.append(i)
#                 find(to_pick-1, picked)
#                 picked.pop()

#     for i in range(1, 11):
#         find(i, [])
#     dec_nums.sort()

#     return dec_nums[n]


# if __name__ == "__main__":
#     N = int(input())
#     if N < LIMIT:
#         print(find_dec_num(N))
#     else:
#         print(-1)


dec_nums = []
