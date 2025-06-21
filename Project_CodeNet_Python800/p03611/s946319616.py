n = int(input())
a = list(map(int, input().split()))

cnt = [0]*(10**5+5)
for i in a:
    cnt[i] += 1

ans = 0
for i in range(1, 10**5+3):
    ans = max(ans, sum(cnt[i-1:i+2]))
print(ans)
