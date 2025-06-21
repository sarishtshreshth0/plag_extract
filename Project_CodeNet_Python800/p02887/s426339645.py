n = int(input())

k = input()

final = 0
for i in range(0, n - 1):
    if k[i] != k[i + 1]:
        final += 1
        
print(final + 1)