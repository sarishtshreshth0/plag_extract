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

n = i()

m = float("Inf")
for i in range( 1,int(n**(1/2))+1 ):
	if n%i == 0:
		note = len(str(max(i,n//i)))
		if note < m:
			m = note
print(m)