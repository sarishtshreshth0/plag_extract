a,b = map(int,input().split())
s = input()
S = list(s)
c = 0
for i in S:
    if i == "-":
        c += 1
        if c > 1:
            print("No")
            exit()
            
if s.isdecimal() is True:
    print("No")
    exit()
    
if len(s) != a + b + 1:
    print("No")
    exit()
    
if s[:a].isdecimal() is True and S[a] == "-":
    print("Yes")
    
else:
    print("No")