n = int(input())
ans, q = 0, ["3", "5", "7"]

while q:
    p = q.pop()
    for s in ["3", "5", "7"]:
        t = p + s
        if int(t) <= n:
            q.append(str(t))
            if len(list(set(list(str(t))))) == 3:
                ans += 1

print(ans)