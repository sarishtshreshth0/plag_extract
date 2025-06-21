"""
int(input())
map(int, input().split())
list(map(int, input().split()))
input()
input().split()
"""

s = input()
cnt = 0
new = s[0]
for i in range(1,len(s)):
    if (s[i]==new[i-1]) : 
        cnt += 1
        new +=  str((int(s[i])+1)%2)
    else: new += s[i]

print(cnt)