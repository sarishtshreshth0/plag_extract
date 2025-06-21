S=[0 if c =='0' else 1 for c in input()]
a = S[0::2]
b = S[1::2]
x = a.count(1)
y = b.count(1)
if x > y:
    ans = (len(a)-x) + (y)
else:
    ans = (len(b)-y) + (x)
print(ans)
