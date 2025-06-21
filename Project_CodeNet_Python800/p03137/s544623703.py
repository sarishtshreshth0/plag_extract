n, m = map(int, input().split())
apple = list(map(int, input().split()))
orange = []
count = 0
if n >= m:
    count = 1
else:
    apple = sorted(apple)
    for i in range(m-1):
        orange.append(apple[i+1] - apple[i])
orange = sorted(orange)

if count == 0:
    if len(orange) != 1:
        if n != 1:
            print(sum(orange[:-(n-1)]))
        else:
            print(sum(orange))
    else:
        print(orange[0])
else:
    print(0)