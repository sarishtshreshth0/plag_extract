s = input()
ev = "10"*(10**5)
od = "01"*(10**5)
evcnt = 0
odcnt = 0
for cnt, i in enumerate(s):
	if i == ev[cnt]:
		evcnt += 1
	if i == od[cnt]:
		odcnt += 1
print(len(s)-max(evcnt, odcnt))