def i():
	return int(input())
def i2():
	return map(int,input().split())
def s():
	return str(input())
def l():
	return list(input())
def intl():
	return list(int(k) for k in input().split())

n,d = i2()
x = []
for i in range(n):
	a = intl()
	x.append(a)

def dist(a,b,d):
	dist = 0
	for i in range(d):
		dist += (a[i] - b[i])**2
	return dist		

cnt = 0
for i in range(n-1):
	for j in range(i+1,n):
		test = dist(x[i], x[j], d)
		if ( (test)**(1/2) )%1 == 0:
			cnt += 1
print(cnt)
