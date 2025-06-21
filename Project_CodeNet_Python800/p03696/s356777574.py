n = int(input())
s = list(input())
l_ins = 0
l = 0
r = 0
for i in range(n):
    if s[i] == "(":
        l += 1
    else:
        r += 1
    l_ins = max(l_ins, r-l)
r_ins = 0
l = 0
r = 0
for i in range(n-1, -1, -1):
    if s[i] == "(":
        l += 1
    else:
        r += 1
    r_ins = max(r_ins, l-r)
ar = ["("]*l_ins + s + [")"]*r_ins
print("".join(ar))


