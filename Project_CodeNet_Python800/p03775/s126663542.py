import math
n=int(input())
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])
    if arr==[]:
        arr.append([n, 1])
    return arr
num=factorization(n)
if len(num)==1:
    if num[0][1]==1:
        ans=num[0][0]
    else:
        ans=num[0][0]*(-(num[0][1]//-2))
    print(len(str(ans)))
else:
    num2=int(math.sqrt(n))
    if num[-1][0]>=num2:
        ans=num[-1][0]
    else:
        for i in range(num2):
            if n%(num2-i)==0:
                ans=n//(num2-i)
                break
    print(len(str(ans)))
