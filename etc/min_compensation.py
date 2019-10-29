"""Minimum Compensation

팔팔 조선소에서는 태풍으로 인한 작업지연으로 수주한 선박들을 기한 내에 완성하지 못할
것이 예상된다. 기한 내에 완성하지 못하면 손해 배상을 해야 하므로 남은 일의 작업량을
숫자로 매기고 배상비용을 최소화하는 방법을 찾으려고 한다.

배상 비용은 각 선박의 완성까지 남은 일의 작업량을 제곱하여 모두 더한 값이 된다.
조선소에서는 1시간 동안 남은 일 중 하나를 골라 작업량 1만큼 처리할 수 있다. 조선소에서
작업할 수 있는 N 시간과 각 일에 대한 작업량이 담긴 배열(works)이 있을 때 배상 비용을
최소화한 결과를 반환하는 함수를 만들라. 예를 들어, N=4일 때, 선박별로 남은 일의 작업량이
works = [4, 3, 3]이라면 배상 비용을 최소화하기 위해 일을 한 결과는 [2, 2, 2]가 되고 배상
비용은 2^2 + 2^2 + 2^2 = 12가 되어 12를 반환해 준다.

[제한사항]
- 일할 수 있는 시간 N : 1,000,000 이하의 자연수
- 배열 works의 크기 : 1,000 이하의 자연수
-각 일에 대한 작업량 : 1,000 이하의 자연수
"""

def min_compensation(time, works):

    length = len(works)

    if time >= sum(works):
        return 0
    
    def do_work(left, works):
        if left == 0:
            return works
        
        max_work = -1
        max_idx = 0
    
        for i in range(length):
            if works[i] >= max_work:
                max_work = works[i]
                max_idx = i
        works[max_idx] -= 1

        return do_work(left-1, works)
    
    do_work(time, works)

    return sum(i**2 for i in works)


if __name__ =="__main__":
    N = int(input())
    works = [int(i) for i in input().split(",")]
    print(min_compensation(N, works))