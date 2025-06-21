#abc057c
n = int(input())
list = []

for ni in range(1,n+1):
    if ni * ni <= n:
        if n % ni == 0:
            list.append(max(len(str(ni)),len(str(n//ni))))
    else:
        break
print(min(list))