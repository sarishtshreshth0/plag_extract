n=int(input())
s=input()
judge=''
for i in range(n):
    if s[i]==judge:
        n-=1
    judge=s[i]

print(n)