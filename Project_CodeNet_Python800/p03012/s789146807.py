import sys
sys.setrecursionlimit(10**6)

n = int(input())
w = list(map(int, input().split()))
#n, m = map(int, input().split())
#s = input()
#s,t = input().split()
#
#readline = sys.stdin.readline
#n,m = [int(i) for i in readline().split()]
#ab = [[int(i) for i in readline().split()] for _ in range(n)]

total = sum(w)
s1 = 0
s2 = total
ans = abs(s1-s2)

for i in w:
    s1 += i
    s2 -= i
    if abs(s1-s2) < ans:
        ans = abs(s1-s2)
        
print(ans)