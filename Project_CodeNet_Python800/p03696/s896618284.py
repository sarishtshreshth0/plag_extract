n = int(input())
s = input()

stock_left = 0
num_new_l = 0
for i in range(n):
    if s[i] == '(':
        stock_left += 1
    else:
        if stock_left > 0:
            stock_left -= 1
        else:
            num_new_l += 1

stock_right = 0
num_new_r = 0
for i in range(-1,-n-1,-1):
    if s[i] == ')':
        stock_right += 1
    else:
        if stock_right > 0:
            stock_right -= 1
        else:
            num_new_r += 1

new_l = '(' * num_new_l
new_r = ')' * num_new_r
print(new_l + s + new_r)