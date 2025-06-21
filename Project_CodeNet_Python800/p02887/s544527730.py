n = int(input())
s = input()
flg = True
pre = '1'
cnt = 0
for c in s:
	if c != pre:
		cnt += 1
		pre = c
print (cnt)