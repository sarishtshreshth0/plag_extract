#第一回日本最強プログラマー学生選手権-予選- a
m,d=map(int,input().split())
ans=0
for month in range(1,m+1):
    for day in range(1,d+1):
        d1=day%10
        d10=day//10
        if d1>=2 and d10>=2 and month==d1*d10:
            ans+=1
print(ans)