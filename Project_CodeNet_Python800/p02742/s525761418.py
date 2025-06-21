n, m = map(int, input().split())

if n == 1 or m == 1:
 print(1)
elif n*m%2 == 0:
 print(n*m//2)
else:
 print(n*m//2+1)