# ABC160 B
x = int(input())
a,moda = divmod(x,500)
b,modb = divmod(moda,5)
print(a*1000+b*5)