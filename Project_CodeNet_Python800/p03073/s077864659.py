a=list(input())
n=[]
for i in range(1,len(a)+1):
    if i%2==0:
        n.append(0)
    else:
        n.append(1)
m=[]
for i in range(1,len(a)+1):
    if i%2==0:
        m.append(1)
    else:
        m.append(0)
ans1=0
for i in range(len(a)):
    if n[i]!=int(a[i]):
        ans1+=1
ans2=0
for i in range(len(a)):
    if m[i]!=int(a[i]):
        ans2+=1
print(min(ans1,ans2))