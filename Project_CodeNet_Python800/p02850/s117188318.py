import sys

sys.setrecursionlimit(10 ** 9)
if __name__ == '__main__':
    n = int(input())
    tree = [[] for i in range(n)]
    for i in range(n - 1):
        a, b = map(int, input().split())
        tree[a - 1].append([b - 1, i])

    ans = 0
    for i in tree:
        ans = max(ans, len(i))

    ans = [0] * (n - 1)


    def solve(cur_index, color):
        cnt = 1

        for to, j in tree[cur_index]:
            if cnt == color:
                cnt += 1
            ans[j] = cnt
            solve(to, cnt)
            cnt += 1


    solve(0, 0)
    print(max(ans))
    print(*ans, sep="\n")