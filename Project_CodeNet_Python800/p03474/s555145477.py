a,b = map(int, input().split())
s = input()
print('Yes' if s[a]=='-' and not('-' in s[:a]+s[a+1:-1]) else 'No')