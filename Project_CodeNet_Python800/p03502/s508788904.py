N = int(input())
x = N
f_X = 0

while x > 0:
    f_X += x % 10
    x //= 10

if N % f_X == 0:
    print("Yes")
else:
    print("No")