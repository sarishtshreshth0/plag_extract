N = int(input())
res = []
arr = list(map(int,input().split()))
for i in range(N-1):
    res.append(abs(sum(arr[:i+1])-sum(arr[i+1:])))
print(min(res))