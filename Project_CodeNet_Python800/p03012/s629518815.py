n = int(input())
w = list(map(int,input().split()))
zentai = sum(w)
ans = sum(w)
suteta = 0

for i in range(n):
    zentai -= w[i]
    suteta += w[i]
    ans = min(ans,abs(zentai-suteta))

print(ans)