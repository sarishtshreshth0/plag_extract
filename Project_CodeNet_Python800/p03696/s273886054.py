n = int(input())
s = input()

d = [0]*(n+1)
for i in range(1, n+1):
    d[i] = s[:i].count('(') - s[:i].count(')')

x = min(d)

s = '('*(-x) + s + ')'*(d[n]-x)
print(s)