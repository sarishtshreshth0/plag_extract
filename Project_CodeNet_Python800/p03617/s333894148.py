q,h,s,d = map(int,input().split())
n = int(input())
print(min(q*n*4,h*n*2,s*n,(n//2)*d+(n%2)*s,(n//2)*d+(n%2)*h*2,(n//2)*d+(n%2)*q*4))