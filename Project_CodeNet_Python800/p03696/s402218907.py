n = input()
s = input().strip()

l = "("
r = ")"

add_right, add_left = 0, 0

for c in s:
    if c == l:
        add_right += 1
    else:
        if add_right:
            add_right -= 1
        else:
            add_left += 1

print(l * add_left + s + r * add_right)