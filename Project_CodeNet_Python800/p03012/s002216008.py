n=int(input()) 
c=list(map(int, input().split()))
t = sum(c)
k = 0
ans =sum(c)

for i in c:
    t -= i
    k += i
    ans = min(abs(t-k),ans)
print(ans)