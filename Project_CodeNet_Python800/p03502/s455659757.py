N=int(input())
X=str(N)
F=0
for i in range(len(X)):
    x=int(X[i])
    F+=x

if N%F==0:
    print("Yes")
else:
    print("No")