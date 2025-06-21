N = int(input())
S = input()

cd = []
q = []
for s in S:
    if q and q[-1]=="(":
        if s==")":
            q.pop()
        else:
            q.append(s)
    else:
        q.append(s)
sl = []
sr = []
for s in q:
    if s==")":
        sl.append("(")
    else:
        sr.append(")")
print("".join(sl)+S+"".join(sr))
