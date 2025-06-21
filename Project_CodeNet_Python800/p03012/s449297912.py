# 129 B

n = int(input())
l = list(map(int, input().split()))
diff = (100 ** 100)

for t in range(len(l)):
    s1 = 0
    s2 = 0

    for i in range(len(l)):
        if i <= t:
            s1 += l[i]
        else:
            s2 += l[i]
    x = abs(s2 - s1)     
    if x <= diff:
        diff = x 
         
print(diff)
    
