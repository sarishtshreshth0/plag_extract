q,h,s,d = map(int,input().split())
n = int(input())
m = min(8*q,4*h,2*s,d)*(n//2) + min(4*q,2*h,s)*(n%2)
print(m)