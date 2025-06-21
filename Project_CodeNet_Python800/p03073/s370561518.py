n = input()
a,b = "",""
for i in range(len(n)//2):
    a += "01"
    b += "10"
if len(n) != len(a):
    a += "0"
    b += "1"

acount,bcount = 0,0
for i in range(len(n)):
    if n[i] != a[i]:
        acount += 1
    if n[i] != b[i]:
        bcount += 1
print(min(acount,bcount))