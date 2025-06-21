N = int(input())
S = list(input())
L = 0
out = []
out2 = []
for i in range(N):
    X = S[i]
    if X=="(":
        L += 1
        out.append("(")
    elif X==")":
        if L>0:
            L += -1
            out.append(")")
        else:
            out2.append("(")
            out.append(")")
for i in range(L):
    out.append(")")
print("".join(out2)+"".join(out))