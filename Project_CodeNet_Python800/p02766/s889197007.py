N, K = map(int, input().split())

i = 0
while True:
    i += 1
    if N // K ** i == 0:
        break
print(i)
