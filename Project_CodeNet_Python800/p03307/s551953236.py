N = int(input())

if N == 1 or N == 2:
    print(2)
else:
    if N % 2 == 0:
        i = N
    else:
        i = N*2
    while i % N != 0:
        i += 2
    print(i)