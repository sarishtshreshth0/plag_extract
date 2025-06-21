import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
ans = float("inf")
for i in range(1,n+1):
    if i**2>n:
        break
    if n%i==0:
        ans = min(ans, max(len(str(i)),len(str(n//i))))
print(ans)