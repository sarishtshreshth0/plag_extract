import sys
A,B = map(int,input().split())
s = str(input())
#print(s[:A],s[A+1:A+B+1],s[A])
if s[A] != '-':
    print("No")
    sys.exit()
elif '-' in s[:A] or '-' in s[A+1:A+B+1]:
    print("No")
else:
    print("Yes")