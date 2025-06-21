n = int(input())
x = 0

a = n

while n > 0:
    x += n%10
    n //=10

if a %x == 0:
    print("Yes")
else:
    print("No")