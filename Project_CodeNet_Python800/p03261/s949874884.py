N=int(input())

W=set()
s="*"
F=True
for _ in range(N):
    H=input()
    if s=="*" or (s==H[0] and H not in W):
        W.add(H)
        s=H[-1]
    else:
        F=False
if F:
    print("Yes")
else:
    print("No")
