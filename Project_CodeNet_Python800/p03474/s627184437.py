A,B=map(int,input().split())
S=input()

N={"0","1","2","3","4","5","6","7","8","9"}
F=True
for i in range(A+B+1):
    if i!=A:
        F&=(S[i] in N)
    else:
        F&=(S[i]=="-")

if F:
    print("Yes")
else:
    print("No")
