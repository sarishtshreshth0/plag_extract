n = int(input())
L = [3,5,7]
for i in range(9):
    P = []
    for p in L:
        a = str(p)+"3"
        P.append(int(a))
        b = str(p)+"5"
        P.append(int(b))
        c = str(p)+"7"
        P.append(int(c))
        
    L.extend(P)
L = list(set(L))
ans = 0
for q in L:
    x = list(str(q))
    if q <= n:
        if "3" in x and "5" in x and "7" in x:
            ans += 1

print(ans)