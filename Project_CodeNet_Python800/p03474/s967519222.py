dic = ["0","1","2","3","4","5","6","7","8","9"]

A,B = map(int,input().split())
S = list(input())

ok = True
for i in range(A):
    if not(S[i] in dic):
        ok=False

if S[A]!="-":
    ok=False

for i in range(A+1,A+B+1,1):
    if not(S[i] in dic):
        ok =False

print("Yes" if ok else"No")
