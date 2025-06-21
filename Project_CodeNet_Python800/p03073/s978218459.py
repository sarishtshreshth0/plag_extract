s = input()
start0 = 0
start1 = 0
for i,j in enumerate(s):
    if ~i&1:
        start0 += (j=="1")
        start1 += (j=="0")
    else:
        start0 += (j=="0")
        start1 += (j=="1")
print(min(start0,start1))