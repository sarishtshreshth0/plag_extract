a, b = map(int, input().split())
n = input()

s1 = n[:a]
s2 = n[a]
s3 = n[a+1:]

if s1.isdigit() and s2=='-' and s3.isdigit():
    print('Yes' , flush=True)
else:
    print('No' , flush=True)
