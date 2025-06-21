def INT():
    return int(input())

def LI():
    return list(map(int, input().split()))

def MI():
    return map(int, input().split())

N, M = MI()
X = LI()
X.sort()

if N >= M:
    print(0)
    exit()

dist = []
for i in range(M - 1):
    d = X[i + 1] - X[i]
    dist.append(d)

dist.sort()
print(sum(dist[ : M - N]))