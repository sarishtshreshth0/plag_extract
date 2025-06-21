N = int(input())
sList = list(input())
count = 0
tmp = ''
for s in sList:
    if(s != tmp):
        count += 1
        tmp = s

print (count)
