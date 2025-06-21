import math

#入力:N,M(int:整数)
def input2():
	return map(int,input().split())

#入力:[n1,n2,...nk](int:整数配列)
def input_array():
	return list(map(int,input().split()))

def euclid(y,z,d):
	result=0
	for i in range(d):
		result+=(y[i]-z[i])**2
	return math.sqrt(result)


n,d=input2()
X=[input_array() for _ in range(n)]

count=0
for i in range(n):
	for j in range(i+1,n):
		distance=euclid(X[i],X[j],d)
		if (distance%1) == 0:
			count+=1
print(count)