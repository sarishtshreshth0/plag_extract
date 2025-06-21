n = int(input())
s = str(input())
p = 0
q = 0
for i in range(n):
    if s[i] == ")":
        if q == 0:
            p += 1
        else:
            q -= 1
    else:
        q += 1
print("("*p+s+")"*q)
