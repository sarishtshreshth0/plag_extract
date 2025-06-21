X = int(input())

sum = 0
gohyakumai =X//500
#print (gohyakumai)
sum = gohyakumai*1000
#print (sum)
goenmai = (X%500)//5
#print (goenmai)
sum = goenmai *5 +sum

print (sum)