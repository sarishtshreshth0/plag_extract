A, B = map(int, input().split())
S = input()
jdg = True
for i, s in enumerate(S):
    if i != A and s not in '0123456789':
        jdg = False
        break
    if i == A and s != '-':
        jdg = False
print('Yes' if jdg else 'No')