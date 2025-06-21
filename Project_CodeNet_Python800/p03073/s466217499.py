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

memo = s[0]
cnt = 0
#print(0,"番目の:",memo)
for i in range(1,len(s)):
	if s[i] == memo:
		cnt += 1
		#print("×")
		if memo == "0":
			memo = "1"
		else:
			memo = "0"
	else:
		memo = s[i]
	#print(i,"番目の:",memo)
print(cnt)