#33
import sys
A,B = map(int,input().split())
S = input()
Ans = "No"
if S[A] != "-":
    print(Ans)
    sys.exit()
    
for i in range(A):
    if S[i] == "-":
        print(Ans)
        sys.exit()

for i in range(A+1,A+B+1):
    if S[i] == "-":
        print(Ans)
        sys.exit()

Ans = "Yes"
print(Ans)

