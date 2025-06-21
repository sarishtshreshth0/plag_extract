n = int(input())

shou500 = n//500

shou5 = (n-shou500*500)//5

print(shou500*1000+shou5*5)