import math

n, x = map(int, input().split())
list_x = list(map(int, input().split()))
list_x.append(x)
list_x.sort()
delta_list = []
for i in range(len(list_x) - 1):
    delta_list.append(list_x[i+1] - list_x[i])
common = delta_list[0]
for num in delta_list:
    common = math.gcd(common, num)
print(common)