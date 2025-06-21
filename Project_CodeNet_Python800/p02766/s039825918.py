N,K = map(int, input().split())

Sum = 0

while True:
    Sum += 1

    if K ** Sum > N:
        break

print(Sum)