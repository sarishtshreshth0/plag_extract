a, b = map(int, input().split())
s = str(input())

s1 = s[:a]
s2 = s[a:a+1]
s3 = s[a+1:]

if s2 == '-':
    if str.isdigit(s1) and len(s1) == a and str.isdigit(s3):
        print('Yes')
    else:
        print('No')
else:
    print('No')