s = list(input())
n = s[0]
p = 0
for i in range(1,len(s)):
    if s[i] == n:
        p += 1
        if s[i] == '0':
            s[i] = '1'
            n = '1'
        else:
            s[i] = '0'
            n = '0'
    else:
        n = s[i] 

print(min(len(s) - p,p))