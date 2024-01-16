"""
n개의 서로 다른 정수로 구성된 집합 S가 있다. 이 집합의 공집합이 아닌 부분집합은 총 2n-1가지 있다. 
각각의 부분집합마다 그 평균을 구한 뒤, 이 2n-1개의 평균들의 평균을 구하는 프로그램을 작성하라. 
 

[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스는 두 개의 줄로 이루어진다. 첫 번째 줄에는 집합의 크기 n (1≤n≤8)이 주어진다. 
두 번째 줄에는 집합 S를 구성하는 n개의 정수가 공백 하나씩을 사이로 두고 주어진다. 각각의 정수는 -1000 이상 1000 이하이다.


[출력]
각 테스트 케이스마다, 부분집합의 평균들의 평균을 한 줄에 하나씩 출력한다. 정답과의 절대 오차 또는 상대 오차가 10-9이하일 시 정답 처리된다. 
평균이 무한소수일 수도 있으므로, 소수점 이하 20 자리 수까지 출력해야 한다. (단, 소수점 이하 0은 출력하지 않는다.
"""

import sys
from itertools import chain, combinations


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(0, len(s)+1))

def powerset_no_empty_set(iterable):
    "powerset([1,2,3]) --> (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s)+1))


def solve(nums):
    subsets = powerset_no_empty_set(nums)
    s = 0
    n = 0

    for subset in subsets:
        s += sum(subset) / len(subset)
        n += 1

    return s / n


def main():
    sys.stdin = open("mean-of-means/input.txt", "r", encoding="utf-8")

    T = int(input())
    for t in range(1, T+1):
        n = int(input())
        nums = set(map(int, input().split(" ")))
        result = solve(nums)
        print(f"#{t} {result}")


if __name__ == "__main__":
    main()
