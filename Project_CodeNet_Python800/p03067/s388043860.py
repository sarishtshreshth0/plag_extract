a,b,c = list(map(int,input().strip().split()))
ans = ()
if a <= c and c <= b:
    ans = ("Yes")
elif b <= c and c <= a:
    ans = ("Yes")
else:
    ans = ("No")
print(ans)