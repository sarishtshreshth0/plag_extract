x = int(input())
yen500 = x//500
yen5 = (x%500)//5
print(1000*yen500 + 5*yen5)