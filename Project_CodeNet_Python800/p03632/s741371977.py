import sys
numbers = sys.stdin.readline().split(' ')

a = int(numbers[0])
b = int(numbers[1])
c = int(numbers[2])
d = int(numbers[3])


if a <= c <= b <= d:
    print(b-c)
elif a <= c <= d <= b:
    print(d-c)
elif c <= a <= d <= b:
    print(d-a)
elif c <= a <= b <= d:
    print(b-a)
else:
    print(0)
