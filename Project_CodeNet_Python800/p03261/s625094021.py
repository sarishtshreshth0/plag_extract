N=int(input())
ok=True
W2=input()
lis=[W2]
for i in range(N-1):
    W=W2
    W2=input()
    if W2 in lis:
        ok=False
        break
    lis.append(W2)
    if(W2[0]!=W[len(W)-1]):
        ok=False
        break
if(ok):
    print("Yes")
else:
    print("No")