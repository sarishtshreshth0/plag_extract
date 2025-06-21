N = int(input())
W = input().split()
W = [int(i) for i in W]

min1 = 10**6
for i in range(N):
    ans = abs(sum(W[:i+1])-sum(W[i+1:]))
    if ans < min1:
        min1 = int(ans)
print(min1)
