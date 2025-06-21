n = int(input())
c,s,f = [],[],[]
for _ in range(n-1):
    x,y,z = map(int,input().split())
    c.append(x)
    s.append(y)
    f.append(z)
    
ans = []
for i in range(n-1): #出発地点
    time = 0
    for j in range(i,n-1): #現在地
        if time <= s[j]:
            time = s[j]+c[j]
        else:
            time += c[j] + f[j]*(0!=time%f[j]) - time%f[j]
    ans.append(time)
        
print('\n'.join(map(str,ans)),'\n0')