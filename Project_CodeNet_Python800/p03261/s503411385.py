N = int(input())
C = {}
flag = 0
for i in range(N):
    W = input().strip()
    if W not in C:
        C[W] = 0
    C[W] += 1
    if i==0:
        a = W
    else:
        if W[0]!=a[-1]:
            flag = 1
        a = W
if len(C)<N or flag==1:
    print("No")
else:
    print("Yes")