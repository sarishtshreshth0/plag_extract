s = input()
oi = "01"*(len(s)//2)
io = "10"*(len(s)//2)
if len(s)%2 == 1:
    oi += "0"
    io += "1"

oans = 0
ians = 0
for i in range(len(s)):
    if s[i] != oi[i]:
        oans += 1
    if s[i] != io[i]:
        ians += 1
print(min(oans, ians))
