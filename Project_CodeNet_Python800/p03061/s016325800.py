n=int(input())
a=list(map(int,input().split()))
size=len(a)
def gcd(a,b):
    while True:
        r=a%b
        if r==0:
            return b
        a,b=b,r
forward=[]
backward=[]
temp=a[0]
for ele in a:
    temp=gcd(temp,ele)
    forward.append(temp)

temp=a[len(a)-1]
for ele in reversed(a):
    temp=gcd(temp,ele)
    backward.append(temp)
backward.reverse()
ans=max(backward[1],forward[len(a)-2])
for i in range(len(a)-2):
    temp=gcd(forward[i],backward[i+2])
    ans=max(ans,temp)
print(ans)

