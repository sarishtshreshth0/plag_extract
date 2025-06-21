A,B = map(int,input().split())
A = A-1
a = A % 2 
b = B % 2

if a == 1:
  A = (A+1)//2%2
else:
  A += (A//2)%2
if b == 1:
  B = (B+1)//2%2
else:
  B += (B//2)%2

ans = [0 for i in range(100)]

bin_a = format(A, 'b')
bin_b = format(B, 'b')

for i in range(len(bin_a)):
  ans[len(bin_a)-i-1] += int( bin_a[i] )
for i in range(len(bin_b)):
  ans[len(bin_b)-i-1] += int( bin_b[i] )
for i in range(100):
  ans[i] = ans[i]%2

a=0
for i in range(100):
  a += ans[i] * (2**i)
print(int(a))