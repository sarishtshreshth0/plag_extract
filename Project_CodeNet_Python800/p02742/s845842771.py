h,k = map(int,input().split())

hh = h%2
kk = k%2

if h == 1 or k == 1:
    ans = 1
elif hh == 0 or kk == 0:
    ans = int(h*k/2)
else:
    ans = int(h*k/2)+1

print(ans)