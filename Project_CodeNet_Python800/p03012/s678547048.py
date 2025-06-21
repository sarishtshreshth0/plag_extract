n = int(input())
w = list(map(int,input().split()))
ans = 10 **10
for i in range(n-1):
    #print(sum(w[:i+1]))
    tmp = abs(sum(w) - 2 * sum(w[:i+1]))
    ans = min(ans,tmp)
print(ans)
