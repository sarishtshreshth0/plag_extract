X = int(input())
quot1, rem = divmod(X,500)
quot2 = rem // 5
print(quot1*1000 + quot2*5)