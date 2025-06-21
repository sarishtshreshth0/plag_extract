x = int(input())
i = 0
while x >= 500:
    x = x - 500
    i = i + 1000
while x >= 5:
    x = x - 5
    i = i + 5
print(int(i))