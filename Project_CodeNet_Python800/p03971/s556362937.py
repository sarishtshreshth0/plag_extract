x = input()
s = input()

n, a, b = map(int, x.split())

p = 0
wp = 0

for char in s:
    if char == 'c' or p >= a+b:
        print('No')
        continue
    if char == 'a':
        p += 1
        print('Yes')
        continue
    if wp < b:
        p += 1
        wp += 1
        print('Yes')
    else:
        print('No')