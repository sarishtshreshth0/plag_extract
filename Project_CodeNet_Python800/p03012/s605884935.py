n = int(input())
w = list(map(int,input().split()))
min_n = 1000 
for m in range(n):
    sum_min = 0
    sum_max = 0
    sum_n = 0
    for i in range(m):
        sum_min += w[i]
    for j in range(m,n):
        sum_max += w[j]
    sum_n = abs(sum_max - sum_min)
    if min_n > sum_n:
        min_n = sum_n
print(min_n)