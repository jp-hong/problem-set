"""
어떠한 문자열 S 가 뒤집어도 S와 동일하다면 S 를 팰린드롬 이라고 하자. 
양의 정수 N, 그리고 N 개의 길이가 같은 문자열이 주어졌을 때, 이들 중 몇 개의 문자열을 고른 후, 
고른 문자열들을 적당히 재배열해서 (문자열을 재배열하는 것이고, 문자열 내부 문자의 순서는 바꿀 수 없다)  순서대로 합쳤을 때 팰린드롬이 되게 해야 한다. 

이 때 최종 팰린드롬의 길이를 최대화해라.

[입력]
첫 번째 줄에 테스트 케이스의 수 TC가 주어진다. 이후 TC개의 테스트 케이스가 새 줄로 구분되어 주어진다. 각 테스트 케이스는 다음과 같이 구성되었다.
첫 번째 줄에 문자열의 개수, 그리고 각 문자열의 길이를 나타내는 두 정수 N, M 이 주어진다. (1≤N≤100, 1≤M≤50)
이후 N 개의 줄에 알파벳 소문자로만 이루어진 길이 M 의 문자열이 주어진다. 주어진 모든 문자열은 서로 다르다. 

[출력]
각 테스트 케이스 마다 한 줄씩 최대화된 팰린드롬의 길이를 출력하라.
"""

import sys


def main():
    def is_palindrome(s):
        return s == s[::-1]

    # def search(s, ls):
    #     if is_palindrome(s):
    #         nonlocal max_len
    #         max_len = max(max_len, len(s))

    #     if len(ls) == 0:
    #         return

    #     search(ls[0] + s, ls[1:])
    #     search(s + ls[0], ls[1:])
    #     search(s, ls[1:])

    def solve(words, l):
        seen = set()
        palindrome = ""
        pairs = []

        for word in words:
            if is_palindrome(word):
                palindrome = word

            if word[::-1] in seen:
                pairs.append((word, word[::-1]))
                seen.remove(word[::-1])
            else:
                seen.add(word)

        return len(palindrome) + len(pairs) * l * 2


    sys.stdin = open("longest-palindrome/input.txt", "r", encoding="utf-8")

    T = int(input())
    for t in range(1, T+1):
        max_len = 0
        n, l = tuple(map(int, input().split(" ")))
        words = []

        for _ in range(n):
            words.append(input())

        max_len = solve(words, l)
        print(f"#{t} {max_len}")


if __name__ == "__main__":
    main()
