n=input()
a = lambda x,y:3**x - y*2**x + y -1+(y%3==0)
ans = 0
ln = len(n)
s = set()
b = True
for p, i in enumerate(n):
    m = int(i) 
    if b:
        if m > 7:
            ans += a(ln-p-1,3-len(s|{7}))
        if m > 5:
            ans += a(ln-p-1,3-len(s|{5}))
        if m > 3:
            ans += a(ln-p-1,3-len(s|{3}))
        if m in (7,5,3):
            s.add(m)
            if ln == p+1:
                ans += len(s)==3
        else:
            b = False
    if ln > p +1:
        ans += a(ln - p -1,3)
print(ans)
