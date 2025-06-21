A,B = map(int,input().split())
S = input()
ans = 'Yes'
if S[A] == '-':
    for i in range(A):
        if not S[i].isdecimal():
            ans = 'No'
    for i in range(A+1,A+B+1):
        if not S[i].isdecimal():
            ans = 'No'
else:
    ans = 'No'
print(ans)