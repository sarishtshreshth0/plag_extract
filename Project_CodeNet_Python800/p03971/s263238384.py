n, a, b = map(int, input().split())
s = input()
count = 0
fs = 0
for i in range(n):
    if s[i] == 'a' and count < a + b:
        print('Yes')
        count += 1
    elif s[i] == 'b' and count < a + b and fs < b:
        print('Yes')
        count += 1
        fs += 1
    else:
        print('No')