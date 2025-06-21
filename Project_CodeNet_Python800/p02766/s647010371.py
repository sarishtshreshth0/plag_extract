from math import log10
n,k=map(int,input().split())
m=int(log10(n)/log10(k))
print(m+1)