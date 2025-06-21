n = int(input())
c = str(n)
a = 0
for i in c:
    a += int(i)
if n % a == 0:
    print("Yes")
else:
    print("No")
