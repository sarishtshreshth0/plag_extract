a,b = map(int, input().split())
s = input()

ok = True
ok = ok and  s[0:a].isdecimal()
ok = ok and s[a] == '-'
ok = ok and s[a+1:].isdecimal()

if ok:
    print("Yes")
else:
    print("No")
