n = int(input())
w = list(map(int, input().split()))

total = sum(w)
dif = 10**5
point = 0

for i in w:
    point += i
    if abs(total-2*point) < dif:
        dif = abs(total-2*point)
    else:
        continue
print(dif)