i = int(input())
a = 0
a += (i // 500) * 1000
i = i % 500
a += (i // 5) * 5
print(a)
