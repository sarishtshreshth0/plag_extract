a, b = map(int, input().split())

if a == b:
    print(a)
    exit()
cnt = b - a + 1
cnt -= (a % 2 == 1) + (b % 2 == 0)
a, b = a * (a % 2 == 1), b * (b % 2 == 0)
if cnt // 2 % 2 == 0:
    print(0 ^ a ^ b)
elif cnt // 2 % 2 == 1:
    print(1 ^ a ^ b)
