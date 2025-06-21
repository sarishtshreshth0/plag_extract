m,d = map(int,input().split())

point = 0

for i in range(1,m+1):
    for j in range(10,d+1):
        s = str(j)
        one = int(s[0])
        two = int(s[1])
        if one >= 2 and two >= 2 and one*two == i:
            point += 1

print(point)