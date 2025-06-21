import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    N = int(input())
    S = input()

    count = 0
    for i in range(N)[::-1]:
        if S[i] == ')':
            count += 1
        else:
            if count:
                count -= 1
            else:
                S += ')'
    S = '('*count + S
    print(S)


if __name__ == '__main__':
    main()
