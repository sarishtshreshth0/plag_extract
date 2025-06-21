S = input()
ss0 = []
ss1 = []
for i in range(len(S)):
    ss0.append(str(i%2))
    ss1.append(str((i+1)%2))

c0 = 0
c1 = 0
for s, s0, s1 in zip(S, ss0, ss1):
    if s != s0:
        c0 += 1
    if s != s1:
        c1 += 1

print(min(c0, c1))