N=int(input())
A=list(map(int, input().split()))

def gcd(a, b):
	while b:
		a, b = b, a%b
	return a

gcd_from_left = [0]*N # 自分のindexは含まないようなもの
gcd_from_right = [0]*N
 
for i in range(1,N):
  gcd_from_left[i] = gcd(A[i-1],gcd_from_left[i-1])
  gcd_from_right[N-1-i] = gcd(A[N-i],gcd_from_right[N-i])
  
ans = 0
 
for a,b in zip(gcd_from_left, gcd_from_right):
  x = gcd(a,b)
  if ans < x:
    ans = x
    
print(ans)