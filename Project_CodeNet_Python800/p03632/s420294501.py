A, B, C, D = list(map(int, input().split()))
if A <= C:
    x = [A, B]
    y = [C, D]
else:
    y = [A, B]
    x = [C, D]
if x[1] <= y[1]:
    d = x[1] - y[0]
else:
    d = y[1] - y[0]
if d < 0:
    d = 0
print(d)