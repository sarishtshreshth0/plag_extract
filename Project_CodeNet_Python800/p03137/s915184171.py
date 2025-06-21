n, m = map(int, input().split())
x = list(map(int, input().split()))
x.sort()

l = []
for i in range(-1,m-1):
    l.append(abs(x[i]- x[i+1]))

l.sort(reverse=True)
print(l[0] - sum(l[1:n]))