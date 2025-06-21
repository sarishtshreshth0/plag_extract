input = list(map(int,input().split()))

a = [input[0], input[1]]
b = [input[2], input[3]]

if a[0] > b[0]:
    a, b = b, a

if a[1] <= b[0]:
    print(0)
elif b[1] <= a[1]:
    print(b[1] - b[0])
else:
    print(a[1] - b[0])