a = int(input())
mini = 10 ** 10
def divisor(n):
    i = 1
    table = []
    while i * i <= n:
        if n%i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    return table
for i in divisor(a):
    i = int(i)
    b = a//i
    maxchecker = max(len(str(i)),len(str(b)))
    mini = min(maxchecker,mini)
print(mini)