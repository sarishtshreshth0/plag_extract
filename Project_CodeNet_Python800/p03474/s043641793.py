a, b = map(int, input().split())
S = input()

if "-" in S[:a] or  "-" in S[a+1:]:
    print("No")
elif "-" == S[a]:
    print("Yes")
else:
    print("No")
