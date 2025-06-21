N,A,B=map(int,input().split())
S=input()

X=A+B
Y=B

T=[]
for s in S:
    if s=="a":
        if X>0:
            T.append(True)
            X-=1
        else:
            T.append(False)
    elif s=="b":
        if X>0 and Y>0:
            T.append(True)
            X-=1
            Y-=1
        else:
            T.append(False)
    else:
        T.append(False)

for t in T:
    if t:
        print("Yes")
    else:
        print("No")
