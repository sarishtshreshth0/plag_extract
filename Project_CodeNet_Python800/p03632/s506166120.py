a,b,c,d = map(int,input().split())
check = min(b,d) - max(a,c)
print(check) if check > 0 else print(0)