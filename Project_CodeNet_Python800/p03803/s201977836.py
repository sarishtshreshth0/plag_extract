A,B=map(int,input().split())
if A==B:
    ans="Draw"
elif A==1 or B==1:
    ans="Alice" if A==1 else "Bob"
else:
    if A<B:
        ans="Bob"
    else:
        ans="Alice"
print(ans)