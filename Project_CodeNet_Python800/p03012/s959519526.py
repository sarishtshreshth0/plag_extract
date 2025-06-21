n = int(input())
W = list(map(int,input().split()))
W_sum = sum(W)
ans = W_sum
num = 0

for i in range(n):
    num += W[i]
    ans = min(ans,abs(2*num-W_sum))
print(ans)
