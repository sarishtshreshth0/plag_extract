q, h, s, d = map(int, input().split())
n = int(input())
n *= 4

lst = [[1, q, q*4], [2, h, h*2], [4, s, s], [8, d, d/2]]
lst.sort(key=lambda x: x[2])

ans = 0
for i in range(4):
    volume = lst[i][0]
    price = lst[i][1]
    ans += price * (n//volume)
    n = n % volume

print(ans)