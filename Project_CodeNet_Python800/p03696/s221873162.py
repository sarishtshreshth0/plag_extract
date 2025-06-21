n = int(input())
s = input()
ss = s
l = 0
for c in ss:
    if c == "(":
        l += 1
    else:
        if l > 0:
            l -= 1
        else:
            s = "(" + s
for i in range(l):
    s = s + ")"
print(s)