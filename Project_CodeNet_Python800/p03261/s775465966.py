N = int(input())
w = ""
S = []
f = True
for i in range(N):
    W = input()
    if i != 0:
        if W[0] != w[(len(w) - 1)] or W in S:
            f = False
            break
    w = W
    S.append(w)
if f == True:
    print("Yes")
else:
    print("No")