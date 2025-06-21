def Level(S):
    A=[0]
    for i in range(len(S)):
        if S[i]=="(":
            A.append(A[-1]+1)
        else:
            A.append(A[-1]-1)
    return A

N=int(input())
S=input()

A=Level(S)
X=-min(A)
T="("*X+S

B=Level(T)
Y=B[-1]
U=T+")"*Y

print(U)