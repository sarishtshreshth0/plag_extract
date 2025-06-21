import sys
sys.setrecursionlimit(9**9)
n=int(input())
T=[[] for _ in range(n)]
for i in range(n-1):
    a,b=map(int,input().split())
    T[a-1].append([b-1,i])
C=[0]*(n-1)
def f(i,r):
    c=1
    for (x,y) in T[i]:
        c+=(c==r)
        C[y]=c
        f(x,c)
        c+=1
f(0,0)
print(max(C))
for c in C:
    print(c)