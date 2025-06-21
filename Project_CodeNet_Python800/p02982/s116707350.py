import sys
n,d = map(int, sys.stdin.readline().rstrip("\n").split())
x = [ [int(s) for s in line.split()] for line in sys.stdin ]
ans = 0
l = [False]*20001
for m in range(1,142):
    l[m*m] = True
for i in range(n):
    for j in range(i+1,n):
        distance = 0
        for dim in range(d):
            distance += (x[i][dim] - x[j][dim])**2
        if l[distance]:
            ans += 1
print(ans)