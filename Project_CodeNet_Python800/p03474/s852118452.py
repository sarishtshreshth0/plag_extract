a, b = map(int, input().split())
s = str(input())
if s[a] == "-":
    if s[:a].isdecimal() == True and s[a+1:].isdecimal() == True:
        print("Yes")
    else:
        print("No")
else:
    print("No")