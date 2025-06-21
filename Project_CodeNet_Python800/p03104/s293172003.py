a, b = map(int, input().split())

def check(n, k):
    if k == 1:
        return ((n + 1) // 2) % 2
    else:
        return max(0, (n + 1) % (k * 2) - k) % 2

k = 1
ans = 0

while k <= b:
    # print(k, check(b, k), check(a, k))
    ans += abs(check(b, k) - check(a-1, k)) % 2 * k
    k *= 2

print(ans)