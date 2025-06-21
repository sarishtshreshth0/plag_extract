m,d = [i for i in input().split()]
ans = 0
for i in range(1,int(m)+1):
    for j in range(1,int(d)+1):
        if (j//10) < 2 or (j%10) < 2:
            pass
        elif i == ((j//10) * (j%10)):
            ans += 1
        else:
            pass
            
print(ans)