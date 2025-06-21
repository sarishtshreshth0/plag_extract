n=int(input())
fx = sum(map(int,list(str(n))))
if n % fx == 0:print('Yes')
else:print('No')