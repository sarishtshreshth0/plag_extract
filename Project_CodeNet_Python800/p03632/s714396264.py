a,b,c,d = map(int,input().split())
a_c = max(a,c)
b_d = min(b,d)
dum = b_d - a_c
if dum < 0:
    print(0)
else:
    print(dum)