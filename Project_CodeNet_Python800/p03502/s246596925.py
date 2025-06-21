n = int(input())
s = str(n)
l = len(s)
sl = list(s)
res=0
for i in range(l):
    res += int(sl[i])

if n % res ==0:
    print("Yes")
else:
    print("No")