n = int(input())
w = list(map(int, input().split()))

ans = 100000000

for i in range(n-1):
    left = sum(w[:i+1])
    right = sum(w[i+1:])
    a = abs(left-right)
    if a<ans:
        ans=a

print(ans)