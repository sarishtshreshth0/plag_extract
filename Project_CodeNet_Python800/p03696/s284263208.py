n = int(input())
sl = list(input())

max_k = 0
now = 0
for s in sl:
    if s == "(":
        now += 1
    else:
        now -= 1
    max_k = min(now, max_k)


print("(" * (-max_k) + "".join(sl) + max(now-max_k, 0) * ")")
