import sys
input = sys.stdin.readline

def divisors(n):
    i = 1
    table = set()
    while i * i <= n:
        if not n % i:
            table.add(i)
            table.add(n//i)
        i += 1
    table = list(table)
    return table

N = int(input())
A = list(map(int, input().split()))

D = divisors(A[0]) + divisors(A[1])
D.sort(reverse=True)
for d in D:
    cnt = 0
    for a in A:
        if a%d:
            cnt += 1
    if cnt <= 1:
        print(d)
        exit()

