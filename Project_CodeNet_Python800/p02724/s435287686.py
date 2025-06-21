x = int(input())
hap = x // 500
hap2 = (x - hap*500)//5
ans = hap*1000 + hap2*5
print(ans)