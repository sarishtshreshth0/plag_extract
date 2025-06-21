n = int(input())
b = [0] * (10 ** 5 + 1)
a = list(map(int, input().split()))
for i in a:
    b[i] += 1
    if i < 10 ** 5:
        b[i + 1] += 1
    if i > 0:
        b[i - 1] += 1

print(max(b))