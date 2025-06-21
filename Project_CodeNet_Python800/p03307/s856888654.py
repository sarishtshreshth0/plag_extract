N = int(input())
index = 1
while True:
    if N % 2 == 0 and N % N == 0:
        print(N)
        break
    else:
        index += 1
        N = index * N