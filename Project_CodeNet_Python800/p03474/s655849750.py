A,B = map(int, input().split())
S = input()

code = S[:A] + S[-B:]

print('Yes' if code.isdecimal() and S[A] == '-' else 'No')