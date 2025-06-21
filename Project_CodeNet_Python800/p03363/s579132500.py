from collections import Counter
n=int(input())
a=list(map(int,input().split()))
def main(n, a):
    s=[0]*(n+1)
    for i in range(n):
        s[i+1]=s[i]+a[i]
    c=Counter(s)
    ans=0
    for value in c.items():
        if value[0]==0:
            ans+=value[1]-1
            if value[1]>2:
                ans+=(value[1]-1)*(value[1]-2)//2
        elif value[1]>1:
            ans+=value[1]*(value[1]-1)//2
    return ans
print(main(n, a))