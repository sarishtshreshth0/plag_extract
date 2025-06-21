a,b = map(int,input().split())
s = input()
if(s[a]=='-'):
    t = s[:a] + s[a+1:a+b]
#     print(t)
    if(t.isdigit()==True):
        print("Yes")
    else:
        print("No")
else:
    print("No")