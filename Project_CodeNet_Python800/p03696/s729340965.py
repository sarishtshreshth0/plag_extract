N = int(input())
S = list(input())
 
f = 0
b = 0
count = 0
for i in range(N - 1, -1, -1):
    if S[i] == '(':
        if count > 0:
            count -= 1
        else:
            b += 1
    else:
        count += 1
 
print('(' * count, end='')
print(*S, sep='', end='')
print(')' * b)