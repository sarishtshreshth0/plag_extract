n = int(input())
nn = n
s = 0
while True:
    mod = n % 10
    s += mod
    n = n // 10
    if n == 0:
        break

if nn % s == 0:
    print("Yes")
else:
    print("No")