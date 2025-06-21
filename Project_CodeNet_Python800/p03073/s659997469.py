s = input()

ans = 100100100100

for i in range(2):
    cnt = 0
    t = str(i)
    for i in s:
        if t != i:
            cnt += 1
            
        t = 1 - int(t)    
        t = str(t)
    
    ans = min(ans,cnt)
    
print(ans)