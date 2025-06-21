A, B = map(int, input().split())
S = input()

if str.isdecimal(S[:A]) and S[A]=="-" and str.isdecimal(S[A+1:]) and len(S[A+1:])==B:
    print("Yes")
else:
    print("No")