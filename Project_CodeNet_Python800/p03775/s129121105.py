# coding = SJIS

n = int(input())
ans = len(str(n))

for i in range(1, int(n ** (1/2)) + 1):
    if i * int((n / i)) == n:
        ans = min(ans, len(str(int(n / i))))
print(ans)