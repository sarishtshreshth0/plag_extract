# 156 B  

n, k = map(int, input().split())
sum = ""
z = n

while z >= 1:
    sum = str((z % k)) + sum
    z = z // k

# print(sum)
print(len(sum))