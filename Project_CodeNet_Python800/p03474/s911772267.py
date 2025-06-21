A, B = map(int, input().split())
S = input()
res = 'Yes'
if not S[:A].isdecimal() or not S[A+1:].isdecimal() or S[A] != '-':
    res = 'No'

print(res)