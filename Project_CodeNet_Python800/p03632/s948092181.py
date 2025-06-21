a , b , c , d = map(int,input().split())

i = max(a,c)
j = min(b,d)
ans = max(0, j - i)
print(ans)