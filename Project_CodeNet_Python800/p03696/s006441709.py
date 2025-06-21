N = int(input())
S = input()

left = 0
for i in range(N - 1, -1, -1):
    if S[i] == ")":
        left += 1
    else:
        left = max(0, left - 1)

right = 0
for i in range(N):
    if S[i] == "(":
        right += 1
    else:
        right = max(0, right - 1)

print("(" * left + S + ")" * right)