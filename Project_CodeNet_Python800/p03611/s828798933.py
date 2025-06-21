import sys
def input(): return sys.stdin.readline().strip()


def main():
    N = int(input())
    A = list(map(int, input().split()))
    S = [0] * (10**5)
    for a in A: S[a] += 1
    ans = max(S[0] + S[1], S[-1] + S[-2])
    for i in range(1, 10**5 - 1):
        ans = max(ans, S[i - 1] + S[i] + S[i + 1])
    print(ans)

if __name__ == "__main__":
    main()
