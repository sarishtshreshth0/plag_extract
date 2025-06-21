A,B = map(int,input().split())
S = input()

count = "No"

if S[:A].isnumeric():
    if S[A] == "-":
        if len(S[A+1:]) == B and S[A+1:].isnumeric():
            count = "Yes"

print(count)