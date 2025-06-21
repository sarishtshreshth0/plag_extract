N = int(input())
n = N
s = 0
for i in range(10):
    a = n % 10
    s += a
    if n // 10 == 0:
        break
    else:
        n = n // 10
if N % s == 0:
    print("Yes")
else:
    print("No")
