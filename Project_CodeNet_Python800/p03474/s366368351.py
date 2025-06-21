a,b = map(int,input().split())
s = input()

print("Yes") if s[0:a].isdigit() and  s[a] == "-" and s[a+1:a+b+1].isdigit() else print("No")