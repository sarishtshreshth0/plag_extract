n=int(input())
lw=[input() for i in range(n)]
used=set()
cond=True
last=lw[0][0]
for w in lw:
    if w in used or last !=w[0]:
        cond=False
        break
    used.add(w)
    last=w[-1]
print("Yes" if cond else "No")