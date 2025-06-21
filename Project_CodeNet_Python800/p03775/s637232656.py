N = int(input())

for i in range(int(N ** 0.5), 0, -1):
    if N % i == 0:
        break

j = N // i
print(len(str(j)))