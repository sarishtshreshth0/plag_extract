N = int(input())
S = list(input())
c = 0
l = []
for i in S:
    if i == "(":
        c += 1
    else:
        c -= 1
    l.append(c)

m = min(l)
if m < 0:
    for i in range(N):
        l[i] += (-m)

    M = l[-1]
    ans = ["("] *(-m) + S + [")"] *M
    
else:
    M = l[-1]
    ans = S + [")"] *M

output = "".join(ans)
print(output)