n = int(input())
ls = list(map(int,input().split()))
max = sum(ls)
k = float("inf")
for i in range(1,n):
    a = sum(ls[:i])
    b = max - a
    if abs(b-a) < k:
        k = abs(b-a)
print(k)
