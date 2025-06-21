# input
N = int(input())

# check
a = N
while a % 2 != 0:
    a += N
else:
    print(a)