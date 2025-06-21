A,B,C,D = map(int,input().split())
counter = 0
for i in range(101):
    if (A <= i < B) and (C <= i < D):
        counter += 1
print(counter)