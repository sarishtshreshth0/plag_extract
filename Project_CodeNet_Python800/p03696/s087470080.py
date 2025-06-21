N = int(input())
S = input()

left = 0
right = 0
left_ans = 0
right_ans = 0
for i in range(N):
    now = S[i]
    if now == "(":
        left += 1
    else:
        right += 1
        if left == 0:
            left_ans += 1
        else:
            left -= 1
            left = max(0, left)
            
S_mirror = ""
for i in range(N-1, -1, -1):
    if S[i] == "(":
        S_mirror += ")"
    else:
        S_mirror += "("

left = 0
right = 0
right_ans = 0
for i in range(N):
    now = S_mirror[i]
    if now == "(":
        left += 1
    else:
        right += 1
        if left == 0:
            right_ans += 1
        else:
            left -= 1
            left = max(0, left)        

ans = "("*left_ans + S + ")"*right_ans
print(ans)