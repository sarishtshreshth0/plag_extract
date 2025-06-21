S = input()

a = ''
for i in range(len(S)//2):
    a += '0'
    a += '1'
if len(S)/2 % 1 != 0:
    a += '0'
b = ''
for i in range(len(S)//2):
    b += '1'
    b += '0'
if len(S)/2 % 1 != 0:
    b += '1'

count_a = 0
for i in range(len(S)):
    if S[i] != a[i]:
        count_a += 1

count_b = 0
for i in range(len(S)):
    if S[i] != b[i]:
        count_b += 1

print(min(count_a, count_b))
