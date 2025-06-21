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

s = s()

cnt0 = 0
cnt1 = 0
for i in range(len(s)):
	if i%2 == 0 :
		if s[i] == "0":
			cnt1 += 1
		else:
			cnt0 += 1
	else:
		if s[i] == "1":
			cnt1 += 1
		else:
			cnt0 += 1
print( min(cnt0, cnt1) )