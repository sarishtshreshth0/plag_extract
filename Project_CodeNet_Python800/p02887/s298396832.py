N=int(input())
S=input()

S=list(S)

ans=[]
color = ''
for s in S:
    if color != s:
        ans.append(s)
        color = s
print(len(ans))