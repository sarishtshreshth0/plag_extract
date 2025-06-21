a,b = map(int,input().split())
s = input()

if s[a] == "-" and s.count("-") == 1:
    if len(s) == a+b+1:
        print("Yes")
    else:
        print("No")
else:
    print("No")