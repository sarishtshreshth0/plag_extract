A, B = map(int, input().split())

A -= 1
ans = 0

def calc(x):
    x += 1
    lst = [0] * 65
    count = 2
    for i in range(64):
        #0の個数を数える
        tmp = x // count
        a = x % count
        a = min(a, count // 2)
        lst[i] = (x - (a + tmp * count // 2)) % 2
        count *= 2
    return lst

lstA = calc(A)
lstB = calc(B)
# print (lstA)
# print (lstB)
tmp = 1
for i in range(65):
    if abs(lstA[i] - lstB[i]) == 1:
        ans += tmp
    tmp *= 2

print (ans)