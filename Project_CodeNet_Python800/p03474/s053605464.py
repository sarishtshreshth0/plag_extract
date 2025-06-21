def func(s, n):
    for i in range(10):
        if s[n] == str(i):
            return True
    return False
  
  
a, b = map(int,input().split())
s = input()

flg = True
if len(s) != a+b+1:
    flg = False

for i in range(a+b+1):
    if i == a:
        if s[i] != '-':
            flg = False
    else:
        flg = func(s, i)
    if not flg:
        break

print('Yes') if flg else print('No')