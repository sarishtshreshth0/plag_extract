N=int(input())
reds=[]
for _ in range(N):
    red=[]
    a,b=map(int,input().split())
    red.append(b)
    red.append(a)
    reds.append(red)
blues=[]
for _ in range(N):
    blue=[]
    c,d=map(int,input().split())
    blue.append(c)
    blue.append(d)
    blues.append(blue)
reds2=sorted(reds)
blues2=sorted(blues)
answer=0
for b in blues2:
    A=[a for a in reds2 if a[1]<b[0] and a[0]<b[1]]
    if len(A)==0:
        continue
    else:
        delete=A[-1]
        reds2.remove(delete)
        answer+=1
print(answer)
