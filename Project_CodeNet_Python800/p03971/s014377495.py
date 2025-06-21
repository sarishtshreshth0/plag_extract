N,A,B = map(int,input().split())
S = input()

D=[]
F = []
ans=[]
f = 0
for i in range(N):
    tmp = S[i]
    if tmp == "a":
        if (len(D)+len(F))<(A+B):
            D.append(tmp)
            ans.append("Yes")
        else:
            ans.append("No")
    elif tmp == "b":
        f += 1
        if (len(D)+len(F))<(A+B) and f<=B:
            F.append(tmp)
            ans.append("Yes")
        else:
            ans.append("No")
    else:
        ans.append("No")

for i in range(N):
    print(ans[i])