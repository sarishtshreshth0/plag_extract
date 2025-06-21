from math import sqrt


def dist(l, m):
    temp = 0
    for i in range(len(l)):
        temp += (l[i] - m[i]) ** 2
    return sqrt(temp).is_integer()


n, d = list(map(int, input().split()))
res = 0
l = []
for _ in range(n):
    l.append(list(map(int, input().split())))
for i in range(n - 1):
    for j in range(i + 1, n):
        res += dist(l[i], l[j])
print(res)
