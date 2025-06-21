A, B = map(int, input().split())
S = input()

ans = "No"

if S[A] == "-":
    if S[:A].isdigit() and S[-B:].isdigit():
        ans = "Yes"
        
print(ans)