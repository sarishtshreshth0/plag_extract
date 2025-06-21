S=input()
A=[]
B=[]
a=0
b=0
for i in range(len(S)):
    if i%2==0:
        A.append("1")
        B.append("0")
    else:
        A.append("0")
        B.append("1")
for i in range(len(S)):
    if A[i]!=S[i]:
        a+=1
    if B[i]!=S[i]:
        b+=1
print(min(a,b))