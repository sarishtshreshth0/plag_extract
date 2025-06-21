from sys import stdin
A,B = [int(x) for x in stdin.readline().rstrip().split()]

def f(n):
    res = 0
    tmp = 1
    while tmp <= n:
        tmp *= 2
        num = ((n+1)//tmp)*(tmp//2)
        num += max(0,(n+1)%tmp - tmp//2)
        if num % 2 != 0:
            res += (tmp//2)
    return res

print(f(A-1)^f(B))