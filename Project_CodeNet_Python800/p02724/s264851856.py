x = int(input())
num = (x//500)*1000
num += ((x%500)//5)*5
print(num)