n = int(input())
d = input()

x = d[0]
count = 1
for i in d:
    if i != x:
        count += 1
        x = i
print(count)