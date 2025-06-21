q,h,s,d = map(int, input().split())
n = int(input())
num = 0
if 2 <= n:
    num += min(8*q,4*h,2*s,d)*(n//2)
    n = n%2
if n == 1:
    num += min(4*q,2*h,s)
print(num)