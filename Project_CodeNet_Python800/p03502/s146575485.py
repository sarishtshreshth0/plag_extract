n = int(input())
summ = sum(list(map(int,str(n))))
if n % summ == 0:
    print("Yes")
else :
    print("No")