n = int(input())
W = list(map(int, input().split()))
sumw = sum(W)
x = 100 * 150
ct = 0
for i in range(n):
    xum = sumw - ct
    sa = abs(xum - ct)
    if sa > x:
        break
    ct += W[i]
    x = sa
print(x)