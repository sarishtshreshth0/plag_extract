a,b=map(int,input().split())
f=lambda x:-(-x//2)%2^x*(x%2^1)
print(f(a-1)^f(b))