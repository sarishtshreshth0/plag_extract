N = int(input())
W = list(map(int,input().split()))

ans = 10**7

for i in range(N-1):
    S1 = W[0:i+1]
    S2 = W[i+1:]
    ans = min(ans,abs(sum(S2)-sum(S1)))

print(ans)