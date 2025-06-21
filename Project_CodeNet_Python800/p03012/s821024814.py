a = int(input())
b = list(map(int,input().split()[:a]))
c = sum(b)
for i in range(len(b)):
    c = min(c, abs(sum(b[:i]) - sum(b[i:])))
print(c)