import math

n=int(input())
ans=10**11
for i in range(1,math.floor(math.sqrt(n)+1)):
    if n%i == 0:
        a=i
        b=n//i
        a_len=len(str(a))
        b_len=len(str(b))
        ans=min(ans,max(a_len,b_len))
print(ans)