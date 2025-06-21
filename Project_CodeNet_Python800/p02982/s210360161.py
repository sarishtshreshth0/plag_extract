import math
N, D = map(int, input().split())
X = []
for n in range(N):
    l = list(map(int, input().split()))
    X.append(l)

def distance(list1, list2):
    s = 0
    for k in range(len(list1)):
        s += (list1[k] - list2[k]) ** 2
    return math.sqrt(s)

ans = 0

for i in range(N-1):
    for j in range(i + 1, N):
        d = distance(X[i], X[j])
        if d.is_integer():
            ans += 1
        else:
            pass

print(ans)