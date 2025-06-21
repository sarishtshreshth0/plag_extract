a, b, c, d = map(int, input().split(" "))

alice = [1 if a <= i < b else 0 for i in range(100)]
bob = [1 if c <= i < d else 0 for i in range(100)]
res = [0 for _ in range(100)]

for i in range(len(res)):
    res[i] = alice[i] * bob[i]

print(sum(res))