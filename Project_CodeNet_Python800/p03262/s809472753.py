from math import gcd
n, x = map(int, input().split())
city = list(map(int, input().split()))
if x not in city:
    city.append(x)
city.sort(reverse=True)
for i in range(len(city) - 1):
    city[i] -= city[i + 1]
ans = city[0]
for i in range(len(city) - 1):
    ans = gcd(ans, city[i])
print(ans)