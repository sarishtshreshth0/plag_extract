n = int(input())
k = 0
k += (n//500)*1000
n = n%500
k += (n//5)*5
print(k)