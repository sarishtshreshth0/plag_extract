N = int(input())
a = list(map(int, input().split()))

count = [0] * (10 ** 5 + 2)

for x in a:
    count[x] += 1
    count[x + 1] += 1
    count[x + 2] += 1
print(max(count))
