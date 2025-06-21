x,y = list(map(float, input().split()))

ansew = x * y

if x == 1 or y == 1:
    print(1)
elif ansew % 2 == 0:
    print(int(ansew / 2))
else:
    print(int(ansew / 2 + 1))