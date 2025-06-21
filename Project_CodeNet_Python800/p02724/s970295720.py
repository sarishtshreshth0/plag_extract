k = input()
k = int(k)

n1 = 0
n2 = 0

while k >= 500:
    n1 += 1
    k -= 500

while k >= 5:
    n2 += 1
    k -= 5

ans = n1 * 1000 + n2 * 5
print(ans)