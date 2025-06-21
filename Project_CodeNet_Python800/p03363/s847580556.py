n = int(input())
a = list(map(int, input().split()))
b = {}
result = 0
a_sum = 0
for i in range(n):
    a_sum += a[i]
    if a_sum in b:
        result += b[a_sum]
        b[a_sum] += 1
    else:
        b[a_sum] = 1
    result += a_sum==0
print(result)