#n = 人数,a = 日本,b = 海外
n,a,b = map(int,input().split())
#s = 順位
s = list(input())
#k = 結果格納
k = []
j = a + b
c = 0
d = 0

for i in range(n):
    if s[i] == 'a':
        if c < j:
            c += 1
            k.append('Yes')
        else:
            k.append('No')
    elif s[i] == 'b':
        if c < j:
            if d < b:
                c += 1
                d += 1
                k.append('Yes')
            else:
                k.append('No')
        else:
            k.append('No')
    else:
        k.append('No')

for i in range(n):
    print(k[i])