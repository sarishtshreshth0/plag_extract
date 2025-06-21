n = int(input())
s = input()

num = [0]
for c in s:
    if c == '(':
        num.append(num[-1] + 1)
    else:
        num.append(num[-1] - 1)

for _ in range(num[0] - min(num)):
    print('(', end='')

print(s, end='')

for _ in range(num[-1] - min(num)):
    print(')', end='')