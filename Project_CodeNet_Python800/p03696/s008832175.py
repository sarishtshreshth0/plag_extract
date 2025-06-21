n = int(input())
s = input()
stack_len = 0
ans = ""
streak = 0
for i in s:
    if i == ")":
        if stack_len:
            stack_len -= 1
            ans += ")"
        else:
            ans = "(" + ans + ")"
    else:
        ans += "("
        stack_len += 1
ans += ")" * stack_len
print(ans)
