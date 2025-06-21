N = int(input())
S_ = input()
s=S_

count = 0
new_left = 0
new_right = 0

for si in s:
    if si == '(':
        count += 1
    else:
        count -= 1

        if count == -1:
            count = 0
            new_left += 1

new_right = count
print('(' * new_left + s + ')' * new_right)