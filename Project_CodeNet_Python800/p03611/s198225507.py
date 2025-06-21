N = int(input())
A = list(map(int, input().split()))
result = {}
for a in A:
    result[a-1] = result.get(a-1, 0) + 1
    result[a] = result.get(a, 0) + 1
    result[a+1] = result.get(a+1, 0) + 1
print(max((result.values())))