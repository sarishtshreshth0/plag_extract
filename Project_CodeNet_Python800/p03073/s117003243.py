S = input().strip()
L = len(S)
p = 0
for i in zip(S, "01"*L):
    if i[0] != i[1]:
        p += 1
q = 0
for i in zip(S, "10"*L):
    if i[0] != i[1]:
        q += 1
print(min(p, q))
