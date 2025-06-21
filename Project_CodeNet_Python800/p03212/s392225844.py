import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    S = readline().strip()
    L = len(S)

    def rec(i, vec, smaller):
        if i == L:
            s = set(vec)
            if 3 in s and 5 in s and 7 in s:
                return 1
            else:
                return 0

        ans = 0
        if not vec:
            ans += rec(i + 1, vec, True)
        if smaller:
            for n in (3, 5, 7):
                vec.append(n)
                ans += rec(i + 1, vec, True)
                vec.pop()
        else:
            for n in (3, 5, 7):
                if n > int(S[i]):
                    break
                vec.append(n)
                if n < int(S[i]):
                    ans += rec(i + 1, vec, True)
                else:
                    ans += rec(i + 1, vec, False)
                vec.pop()

        return ans

    ans = rec(0, [], False)

    print(ans)
    return


if __name__ == '__main__':
    main()
