x = int(input())
y = [int(z) for z in input().split()]
m = 100000000000000
s = sum(y)
for i in range(x):
      m = min(m, abs(sum(y[i+1:])-sum(y[:i+1])))
print(m)
