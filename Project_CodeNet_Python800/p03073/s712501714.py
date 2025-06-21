import sys
import copy

stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def switch(s):
    if s == '0':
        return '1'
    else:
        return '0'


def main():
    S = list(input())
    S_1 = copy.copy(S)
    S_2 = copy.copy(S)
    ans_1 = 0
    for i in range(1, len(S_1)):
        if S_1[i] == S_1[i - 1]:
            S_1[i] = switch(S_1[i])
            ans_1 += 1
    ans_2 = 1
    S_2[0] = switch(S_2[0])
    for i in range(1, len(S_2)):
        if S_2[i] == S_2[i - 1]:
            S_2[i] = switch(S_2[i])
            ans_2 += 1
    print(min(ans_1, ans_2))


if __name__ == '__main__':
    main()
