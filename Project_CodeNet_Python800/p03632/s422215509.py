import sys

numbers = sys.stdin.readline().split(' ')

a = int(numbers[0])
b = int(numbers[1])
c = int(numbers[2])
d = int(numbers[3])

dist = min(b,d) - max(a,c)
if dist < 0:
    print(0)
else:
    print(dist)