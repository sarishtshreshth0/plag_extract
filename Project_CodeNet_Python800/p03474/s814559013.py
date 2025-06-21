a,b = map(int,input().split())
s = input()
s1 = s[0:a]
s2 = s[a]
s3 = s[a + 1:a + b + 1]
if "-" not in s1 and s2 == "-" and "-" not in s3:
    print("Yes")
else:
    print("No")
