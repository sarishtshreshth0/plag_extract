M,D=map(int, input().split())
print(sum(d%10>=2 and d//10>=2 and d%10*(d//10)<=M for d in range(1, D+1)))