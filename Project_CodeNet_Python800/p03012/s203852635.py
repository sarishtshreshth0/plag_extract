n = int(input())
w = list(map(int, input().split()))
ans = []
for i in range(n):
    x = abs(sum(w[:i])-sum(w[i:]))
    ans.append(x)
print(min(ans))