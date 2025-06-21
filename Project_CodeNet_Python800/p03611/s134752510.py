N = int(input())
a = map(int, input().split())

x = [0]*(10**5 + 2)
for i in a:
    x[i-1] += 1
    x[i] += 1
    x[i+1] += 1

res = max(x)
print(res)
