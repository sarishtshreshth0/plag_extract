#b
A,B=map(int,input().split())
S=input()

sa = S[:A]
sb = S[A+1:]

if sa.isdecimal() and sb.isdecimal() and S[A]=="-":
    print("Yes")
else:
    print("No")