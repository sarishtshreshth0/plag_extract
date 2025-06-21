input()
s = input()
d = 0
x = 0
for c in s:
    if c == "(":
        d += 1
    else:
        d -= 1
    x = min(d, x)
print("(" * -x + s + ")" * (d - x))