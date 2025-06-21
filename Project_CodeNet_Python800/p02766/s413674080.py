N,K = map(int,input().split())
count = 0
a = int(N / K)
while a > 0:
  a = int( a / K ) 
  count += 1
print( count + 1 )