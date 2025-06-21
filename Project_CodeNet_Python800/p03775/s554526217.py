N = int(input()) 
ans = 111111111110
for i in range(1,int(N**0.5+2)):
    if N%i == 0:
        use = N//i 
        s = str(use) 
        t = str(i) 
        ans = min(ans, max(len(s), len(t))) 

print(ans)