n = int(input())
w = [int(x) for x in input().split()]

t = int(n/2)
s1 = sum(w[0:t])
s2 = sum(w[t:n])

if s1 == s2:print(0)
else:
    if s1<s2: a=1
    if s1>s2: a=-1
    out = abs(s1-s2)

    for xi in range(n):
        t = t+a
        if a == 1:
            s1 += w[t-1]
            s2 -= w[t-1]
        if a ==-1:
            s1 -= w[t]
            s2 += w[t]
        if out<abs(s1-s2):break
        out = abs(s1-s2)

print(out)
