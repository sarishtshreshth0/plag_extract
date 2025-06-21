import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


m,d = list(map(int, input().split()))
ans = 0
for i in range(1, m+1):
    for j in range(1, d+1):
        if j<10:
            continue
        d1 = int(str(j)[0])
        d2 = int(str(j)[1])
        if d1*d2==i and d1>=2 and d2>=2:
            ans += 1
print(ans)