n = int(input())
s = input()

num = n
for i in range(n-1,0,-1):
    if s[i]==s[i-1]:
        s = s[:i] + s[i+1:]
    
print(len(s))     
