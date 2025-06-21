def gcd(a,b):
	if b==0:
		return a
	else:
		return gcd(b,a%b)

N=int(input())
array=sorted([int(x) for x in input().split()])
prefix_GCD=[0]*(N)
suffix_GCD=[0]*(N)
currentGCD=array[0]

for i in range(N):
	prefix_GCD[i]=gcd(currentGCD,array[i])
	currentGCD=gcd(currentGCD,(array[i]))
currentGCD=array[N-1]

for i in range(N-1,-1,-1):
	suffix_GCD[i]=gcd(currentGCD,(array[i]))
	currentGCD=gcd(currentGCD,(array[i]))
	
highest=0
for i in range(N):
	if i==0:
		gcdwithout=suffix_GCD[1]
	elif i==N-1:
		gcdwithout=prefix_GCD[-2]
	else:
		gcdwithout=gcd(prefix_GCD[i-1],suffix_GCD[i+1])
	highest=max(highest,gcdwithout)
print(highest)