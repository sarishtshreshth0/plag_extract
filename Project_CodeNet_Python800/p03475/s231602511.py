n = int(input())
csf = [[int(i) for i in input().split()] for _ in range(n - 1)]


def get(i):
    ans = 0
    for c, s, f in csf[i:]:
        ans = max(ans, s)
        ans = (ans + f - 1) // f * f
        ans += c
    return ans


for i in range(n):
    print(get(i))
