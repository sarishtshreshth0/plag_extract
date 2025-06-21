A,B=map(int,input().split())
S=str(input())
ans="Yes"
num="0","1","2","3","4","5","6","7","8","9"
for i in range(A+B+1):
    if i<A:
        if S[i] not in num:
            ans="No"
            break
    elif i==A:
        if S[i]!="-":
            ans="No"
            break
    elif i<=A+B:
        if S[i] not in num:
            ans="No"
            break
print(ans)