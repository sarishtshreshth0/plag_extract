S = list(map(int, input()))
a = [0 if (i+1)%2 == 0 else 1 for i in range(len(S))]
b = [0 if (i+1)%2 == 1 else 1 for i in range(len(S))]
ans0, ans1 = 0, 0
ans0 = [0 for i, j in zip(a, S) if i == j]
ans1 = [0 for i, j in zip(b, S) if i == j]
print(min(len(ans0), len(ans1)))
