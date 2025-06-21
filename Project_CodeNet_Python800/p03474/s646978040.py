import sys
A,B=map(int,input().split())
S=input()
for i in range(A):
    try:
        num=int(S[i])
    except:
        print("No")
        sys.exit()
if S[A]!="-":
    print("No")
    sys.exit()
for i in range(B):
    try:
        num=int(S[i+A+1])
    except:
        print("No")
        sys.exit()
print("Yes")