n = int(input())

ans = 0
for i in list(range(1,int(n**0.5)+1))[::-1]:
    if n%i == 0:
        print(len(str(i)) if i > n/i else len(str(n//i)))
        exit()
print(len(str(n)))