a,b=map(int,input().split())
s=input()

if "-" in s[:a] or "-" in s[-b:] or s[a]!="-":
    print("No")
else:
    print("Yes")