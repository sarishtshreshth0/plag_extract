n = int(input())
li = [list(map(int,input().split())) for i in range(n-1)] #csf

for i in range(n-1):
    t = li[i][1] + li[i][0]
    for j in range(i+1,n-1):
        while True:
            if t >= li[j][1] and t%li[j][2] == 0:
                break
            else:
                t += 1
        t += li[j][0]
    print(t)
print(0)