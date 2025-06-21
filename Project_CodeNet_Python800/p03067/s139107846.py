a,b,c=map(int,input().split())
ab=[i for i in range(min(a,b),max(a,b)+1)]
print('Yes' if c in ab else 'No')