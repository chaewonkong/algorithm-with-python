"""카카오 코드 페스티벌

Baekjoon No.15953
URL: https://www.acmicpc.net/problem/15953

제이지는 자신이 코드 페스티벌에 출전하여 받을 수 있을 상금이 얼마인지 궁금해졌다. 
그는 자신이 두 번의 코드 페스티벌 본선 대회에서 얻을 수 있을 총 상금이 
얼마인지 알아보기 위해, 상상력을 발휘하여 아래와 같은 가정을 하였다.

제1회 코드 페스티벌 본선에 진출하여 a등(1 ≤ a ≤ 100)등을 하였다. 
단, 진출하지 못했다면 a = 0으로 둔다.

제2회 코드 페스티벌 본선에 진출하여 b등(1 ≤ b ≤ 64)등을 할 것이다. 
단, 진출하지 못했다면 b = 0으로 둔다.

제이지는 이러한 가정에 따라, 자신이 받을 수 있는 총 상금이 얼마인지를 알고 싶어한다.

[1회]
순위  상금	인원
1등	500만원	1명
2등	300만원	2명
3등	200만원	3명
4등	50만원	4명
5등	30만원	5명
6등	10만원	6명

[2회]
순위  상금	인원
1등 512만원	1명
2등	256만원	2명
3등	128만원	4명
4등	64만원	8명
5등	32만원	16명

[입력]
첫 번째 줄에 제이지가 상상력을 발휘하여 가정한 횟수 T(1 ≤ T ≤ 1,000)가 주어진다.

다음 T개 줄에는 한 줄에 하나씩 제이지가 해본 가정에 대한 정보가 주어진다. 
각 줄에는 두 개의 음이 아닌 정수 a(0 ≤ a ≤ 100)와 b(0 ≤ b ≤ 64)가 
공백 하나를 사이로 두고 주어진다.

[출력]
각 가정이 성립할 때 제이지가 받을 상금을 원 단위의 정수로 한 줄에 하나씩 출력한다. 
입력이 들어오는 순서대로 출력해야 한다.

[예제입력]
6
8 4
13 19
8 10
18 18
8 25
13 16

[예제출력]
1780000
620000
1140000
420000
820000
620000
"""

first_rewards = [5000000, 3000000, 2000000, 500000, 300000, 100000]
first_winners = [1, 2, 3, 4, 5, 6]
second_rewards = [5120000, 2560000, 1280000, 640000, 320000]
second_winners = [1, 2, 4, 8, 16]

def get_reward(ranking, rewards, winners):
    """Return reward for given ranking."""
        
    if ranking == 0 or ranking > sum(winners):
        return 0
    else:
        for i in range(len(winners)):
            if sum(winners[:i+1]) >= ranking:
                return rewards[i]


if __name__ == "__main__":
    T = int(input())
    results = []
    
    # Calculate total Reward and store result in results list.
    for _ in range(T):
        first_rank, second_rank = [int(i) for i in input().split(" ")] 
        result = get_reward(first_rank, first_rewards, first_winners) + get_reward(second_rank, second_rewards, second_winners)
        results.append(result)
    for result in results:
        print(result) 